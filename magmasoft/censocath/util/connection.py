# -*- coding: utf-8 -*-

'''
Created on 06/12/2012

@author: Carlos
'''

from PyQt4 import QtSql
import logging

class Connection(object):
    '''
    classdocs
    '''

    logger = logging.getLogger("daos")


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @staticmethod
    def createConnection():
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("database/censocath")
        if not db.open():
            Connection.logger.error("no se pudo abrir la base de datos")
        else:
            Connection.logger.info("se pudo abrir la base de datos")
        pass
