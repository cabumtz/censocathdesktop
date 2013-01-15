#-*- coding:utf-8 -*-

import sip

# import this
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

# These are only needed for Python v2 but are harmless for Python v3.
from PyQt4 import QtCore, QtGui
from magmasoft.censocath.util.encoding import _fromUtf8
from magmasoft.censocath.factories import ServiceFactory
from magmasoft.censocath.model.sqlmodel import FamiliaModel
from magmasoft.censocath.model.sqlmodel import IntegrantesFamiliaModel
from magmasoft.censocath.util.connection import Connection
from magmasoft.censocath.view.ui_encuestadialog import Ui_WzrdEncuesta
from magmasoft.censocath.view.ui_mainwindow import Ui_MainWindow
from magmasoft.censocath.view.ui_wzrdpgdatosgenerales import Ui_WzrdPgDatosGenerales
from magmasoft.censocath.view.ui_wzrdpgdatosintegrantes import Ui_WzrdPgDatosIntegrantes







class WzrdPgDatosGenerales(QtGui.QWizardPage):
    
    def __init__(self, parent=None):
        super(WzrdPgDatosGenerales, self).__init__(parent)
        self.ui = Ui_WzrdPgDatosGenerales()
        self.ui.setupUi(self)
        self.__initialize()
        
        pass
    
    def __initialize(self):
        
        pass
    
    def showEvent(self, *args, **kwargs):
        self.reloadCmbBxEncuestadores()
        return QtGui.QWizardPage.showEvent(self, *args, **kwargs)
    
    def reloadCmbBxEncuestadores(self):
        # clean the combobox items
        self.ui.cmbBxEncuestador.clear()
        servicefactory = ServiceFactory.getInstance() 
        encuestadores = servicefactory.getEncuestadorService().getAllEncuestadores()
        
        # adding elements to the combobox
        self.ui.cmbBxEncuestador.addItem("<selecciona o escribe>", -1)
        for enc in encuestadores :
            self.ui.cmbBxEncuestador.addItem(enc.nombre, enc.identifier )
            pass


class WzrdPgDatosIntegrantes(QtGui.QWizardPage):
    
    def __init__(self, parent=None):
        super(WzrdPgDatosIntegrantes, self).__init__(parent)
        self.ui = Ui_WzrdPgDatosIntegrantes()
        self.ui.setupUi(self)
        self.__initialize()
        pass
    
    def __initialize(self):
        self.model = IntegrantesFamiliaModel()
        self.ui.tblVwFamiliares.setModel(self.model)
        pass
    
    def realoadIntegrantesFamiliaModel(self):
        
        pass
    

class EncuestaDialogForm(QtGui.QWizard):
    
    def __init__(self, parent=None):
        super(EncuestaDialogForm, self).__init__(parent)
        self.ui = Ui_WzrdEncuesta()
        self.ui.setupUi(self)
        self.__initialize()
        pass
    
    def __initialize(self):
        self.addPage( WzrdPgDatosGenerales(self) )
        self.addPage( WzrdPgDatosIntegrantes(self) )
        #self.setWizardStyle(QtGui.QWizard.MacStyle)
        #self.setWizardStyle(QtGui.QWizard.ModernStyle)
        #self.setPixmap(QtGui.QWizard.WatermarkPixmap, QtGui.QPixmap(_fromUtf8(":/background/images/imgs/familia_cristiana2.jpg")))
        #self.setPixmap(QtGui.QWizard.BackgroundPixmap, QtGui.QPixmap(_fromUtf8(":/background/images/imgs/familia_cristiana2.jpg")))
        pass


class MainWindowForm(QtGui.QMainWindow):
    __familiaModel = None
    __wzrdEncuesta = None
    
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        
        # prepare database before gui
        self.__initDatabase()
        
        # prepare gui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.__initialize()
        
        pass
    
    
    @QtCore.pyqtSlot(bool)
    def on_salir_triggered(self):
        """mb = QtGui.QMessageBox()
        mb.setText("una prueba")
        mb.exec_()"""
        QtGui.QApplication.quit()
        pass
    
    @QtCore.pyqtSlot(bool)
    def on_new_encuesta_triggered(self):
        
        self.__wzrdEncuesta.show()
        pass
    
    def __initDatabase(self):
        Connection.createConnection()
        pass
    
    def __initialize(self):
        
        self.__familiaModel = FamiliaModel( )
        self.ui.tblVwEncuestas.setModel(self.__familiaModel)
        
        self.ui.actionSalir.triggered.connect(self.on_salir_triggered)
        self.ui.actionNueva_Encuesta.triggered.connect(self.on_new_encuesta_triggered)
        
        self.__wzrdEncuesta = EncuestaDialogForm(self)
        
        pass
    


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    mainwindow = MainWindowForm()
    mainwindow.show()
    sys.exit(app.exec_())

