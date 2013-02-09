# -*- coding: utf-8 -*-

'''
Created on 08/01/2013

@author: Carlos
'''
from magmasoft.censocath.daos import EncuestadorDao
from magmasoft.censocath.services import EncuestadorService



class ServiceFactory(object):
    
    instance = None
    
    def __init__(self):
        encuestadorDao = EncuestadorDao()
        self.daos = {
                     "encuestadorDao" : encuestadorDao,
                      }
        
        
        self.encuestadorService = EncuestadorService(self.daos)
        
        pass
    
    
    @staticmethod
    def getInstance():
        if (ServiceFactory.instance == None) :
            ServiceFactory.instance = ServiceFactory()
             
        return ServiceFactory.instance
    
    
    def getEncuestadorService(self):
        return self.encuestadorService
    
        
    pass


