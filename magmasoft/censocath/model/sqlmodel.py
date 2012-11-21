'''
Created on 14/11/2012

@author: Carlos
'''

# These are only needed for Python v2 but are harmless for Python v3.
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui, QtSql

class FamiliaModel(QtSql.QSqlQueryModel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    def flags(self, index):
        flags = super(FamiliaModel, self).flags(index)
        
        if index.column() in (1, 2):
            flags |= QtCore.Qt.ItemIsEditable

        return flags
    
    def setData(self, index, value, role):
        if index.column() not in (1, 2):
            return False

        primaryKeyIndex = self.index(index.row(), 0)
        id = self.data(primaryKeyIndex)

        self.clear()

        if index.column() == 1:
            ok = self.setFirstName(id, value)
        else:
            ok = self.setLastName(id, value)

        self.refresh()
        return ok

    def refresh(self):
        self.setQuery('select * from person')
        self.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        self.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")

    def setFirstName(self, personId, firstName):
        query = QtSql.QSqlQuery()
        query.prepare('update person set firstname = ? where id = ?')
        query.addBindValue(firstName)
        query.addBindValue(personId)
        return query.exec_()

    def setLastName(self, personId, lastName):
        query = QtSql.QSqlQuery()
        query.prepare('update person set lastname = ? where id = ?')
        query.addBindValue(lastName)
        query.addBindValue(personId)
        return query.exec_()