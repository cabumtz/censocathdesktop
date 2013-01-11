'''
Created on 04/01/2013

@author: Carlos
'''
from PyQt4 import QtSql
from magmasoft.censocath.vos import Encuestador

import logging

class EncuestadorDao(object):
    '''
    classdocs
    '''
    
    logger = logging.getLogger("daos")


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    def getAllEncuestadores(self):
        '''
        '''
        strQuery = """
            SELECT 
              e."Id" AS "Id", e."Nombre" AS "Nombre"
            FROM
              "Encuestador" e
            ORDER BY
              e."Nombre" ASC
            """
        encuestador = None
        
        query = QtSql.QSqlQuery()
        query.setForwardOnly(True)
            
        if( not query.prepare( strQuery ) ) :
            # there was an error
            # right now I don't know what to do
            EncuestadorDao.logger.error( "Error al preparar SQL: %s" % query.lastError().text() )
            pass
    
        EncuestadorDao.logger.debug( "SQL: %s" % strQuery )
    
        if( not query.exec_() ) :
            # there was an error
            # right now I don't know what to do
            EncuestadorDao.logger.error( "Error al ejecutar SQL: %s" % query.lastError().text() )
            pass
        
        resultList = []    
        while ( query.next() ) :
            encuestador = Encuestador()
            encuestador.identifier = query.value(0)
            encuestador.nombre = query.value(1)
            EncuestadorDao.logger.debug("encuestador: %d, %s" % ( encuestador.identifier, encuestador.nombre) )
            resultList.append(encuestador)
            pass
        
        return resultList

