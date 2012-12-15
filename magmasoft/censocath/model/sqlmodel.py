'''
Created on 14/11/2012

@author: Carlos
'''

# These are only needed for Python v2 but are harmless for Python v3.
import sip
import this
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore, QtGui, QtSql


# FamiliaModel

class FamiliaModel(QtSql.QSqlQueryModel):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FamiliaModel, self).__init__()
        
        self.setQuery("""
            SELECT
              fa."Id" AS "Id", co."Nombre" AS "Colonia", ca."Nombre" AS "Calle", fa."Lote" AS "Lote",
              fa."NoExt" AS "NoExt", fa."NoInt" AS "NoInt" 
            FROM
              "Familia" AS fa INNER JOIN
              "Calle" AS ca ON ca."Id" = fa."IdCalle" INNER JOIN
              "Manzana" AS ma ON ma."Id" = fa."IdManzana" INNER JOIN
              "Colonia" AS co ON co."Id" = ca."IdColonia"
            """)
        pass
    
    
    def flags(self, index):
        flags = super(FamiliaModel, self).flags(index)
        
        flags &= ( ~ (QtCore.Qt.ItemIsEditable) )
        return flags



# IntegrantesFamiliaModel

class IntegrantesFamiliaModel(QtSql.QSqlQueryModel):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IntegrantesFamiliaModel, self).__init__()
        
        self.setQuery("""
            SELECT
              p."Id" AS "Id", p."Nombre" AS "Nombre", pa."Nombre" AS "Parentesco", p."Edad" AS "Edad", re."Nombre" AS "Religion"
            FROM
              "Persona" p INNER JOIN
              "Parentesco" pa ON p."IdParentesco" = pa."Id" INNER JOIN
              "Religion" re ON p."IdReligion" = re."Id"
            --WHERE
            --  p."IdFamilia" = 1
            """)
        pass
    
    
    def flags(self, index):
        flags = super(IntegrantesFamiliaModel, self).flags(index)
        
        flags &= ( ~ (QtCore.Qt.ItemIsEditable) )
        return flags

