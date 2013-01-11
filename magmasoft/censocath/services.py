'''
Created on 08/01/2013

@author: Carlos
'''
class EncuestadorService(object):
    
    
    def __init__(self, daos):
        self.daos = daos
        pass
    
    def getAllEncuestadores(self):
        encuestadorDao = self.daos["encuestadorDao"]
        return encuestadorDao.getAllEncuestadores()
    
    pass