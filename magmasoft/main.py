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
from magmasoft.censocath.view.ui_wzrdpgdatosfamilia import Ui_WzrdPgDatosFamilia
from magmasoft.censocath.view.ui_wzrdpgdatosintegrantes import Ui_WzrdPgDatosIntegrantes
from magmasoft.censocath.view.ui_wzrdpgresumen import Ui_WzrdPgResumen


import logging


logger = logging.getLogger("gui")

class WzrdPgDatosGenerales(QtGui.QWizardPage):
    
    def __init__(self, parent=None):
        super(WzrdPgDatosGenerales, self).__init__(parent)
        
        self.__initialize()
        
        pass
    
    def __initialize(self):
        self.ui = Ui_WzrdPgDatosGenerales()
        self.ui.setupUi(self)
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
        self.ui.cmbBxEncuestador.addItem("-- Seleccione --", -1)
        for enc in encuestadores :
            self.ui.cmbBxEncuestador.addItem(enc.nombre, enc.identifier )
            pass


class WzrdPgDatosFamilia(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(WzrdPgDatosFamilia, self).__init__(parent)
        self.__initialize()
        pass
    
    def __initialize(self):
        self.ui = Ui_WzrdPgDatosFamilia()
        self.ui.setupUi(self)    
        pass
    
    pass

class WzrdPgDatosIntegrantes(QtGui.QWizardPage):
    
    def __init__(self, parent=None):
        super(WzrdPgDatosIntegrantes, self).__init__(parent)
        self.__initialize()
        pass
    
    def __initialize(self):
        self.ui = Ui_WzrdPgDatosIntegrantes()
        self.ui.setupUi(self)
        self.model = IntegrantesFamiliaModel()
        self.ui.tblVwFamiliares.setModel(self.model)
        self.movSplitterBottom()
        self.ui.tlBttnNuevo.toggled.connect(self.on_nuevoIntegrante_toggled)
        #self.ui.spltterSplitter.splitterMoved.connect(self.on_splitter_moved)
        
        
        
        
        pass
    
    def realoadIntegrantesFamiliaModel(self):
        
        pass
    
    def movSplitterTop(self):
        self.ui.spltterSplitter.moveSplitter (0, 1)
        pass
    
    def movSplitterBottom(self):
        self.ui.spltterSplitter.moveSplitter ((self.ui.spltterSplitter.getRange(1))[1], 1)
        pass
    
    def movSplitterMiddle(self):
        self.ui.spltterSplitter.moveSplitter ((self.ui.spltterSplitter.getRange(1))[1] / 2, 1)
        pass

    @QtCore.pyqtSlot(bool)
    def on_nuevoIntegrante_toggled(self, checked):
        """
        """
        logger.debug("on_nuevoIntegrante_toggled - checked: %s" % checked)
        #logger.debug( "Rango del splitter: %s, %s" % self.ui.spltterSplitter.getRange(1) )
        
        if checked :
            self.movSplitterTop()
        else :
            self.movSplitterBottom()
            
        
        
        pass
    
    @QtCore.pyqtSlot(int, int)
    def on_splitter_moved(self, pos, index):
        logger.debug("on_splitter_moved - pos: %s, index: %s" % (pos, index) )
        pass



class WzrdPgResumen(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(WzrdPgResumen, self).__init__(parent)
        self.__initialize()
        pass
    
    def __initialize(self):
        self.ui = Ui_WzrdPgResumen()
        self.ui.setupUi(self)    
        pass
    
    pass


class EncuestaDialogForm(QtGui.QWizard):
    
    def __init__(self, parent=None):
        super(EncuestaDialogForm, self).__init__(parent)
        
        self.__initialize()
        pass
    
    def __initialize(self):
        self.ui = Ui_WzrdEncuesta()
        self.ui.setupUi(self)
        
        # pages
        self.addPage( WzrdPgDatosGenerales(self) )
        self.addPage( WzrdPgDatosFamilia(self) )
        self.addPage( WzrdPgDatosIntegrantes(self) )
        self.addPage( WzrdPgResumen(self) )
        
        # buttons
        self.setButtonText(QtGui.QWizard.BackButton, QtGui.QApplication.translate("EncuestaDialogForm", "Atrás", None, QtGui.QApplication.UnicodeUTF8))
        self.setButtonText(QtGui.QWizard.NextButton, QtGui.QApplication.translate("EncuestaDialogForm", "Adelante", None, QtGui.QApplication.UnicodeUTF8))
        self.setButtonText(QtGui.QWizard.FinishButton, QtGui.QApplication.translate("EncuestaDialogForm", "Finalizar", None, QtGui.QApplication.UnicodeUTF8))
        self.setButtonText(QtGui.QWizard.CommitButton, QtGui.QApplication.translate("EncuestaDialogForm", "Comprometer", None, QtGui.QApplication.UnicodeUTF8))
        self.setButtonText(QtGui.QWizard.CancelButton, QtGui.QApplication.translate("EncuestaDialogForm", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.setButtonText(QtGui.QWizard.HelpButton, QtGui.QApplication.translate("EncuestaDialogForm", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        
        #self.setWizardStyle(QtGui.QWizard.MacStyle)
        self.setWizardStyle(QtGui.QWizard.ModernStyle)
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
        self.__initialize()
        
        pass

    def __initDatabase(self):
        Connection.createConnection()
        pass
    
    def __initialize(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.__familiaModel = FamiliaModel( )
        self.ui.tblVwEncuestas.setModel(self.__familiaModel)
        
        self.ui.actionSalir.triggered.connect(self.on_salir_triggered)
        self.ui.actionNueva_Encuesta.triggered.connect(self.on_new_encuesta_triggered)
        
        self.__wzrdEncuesta = EncuestaDialogForm(self)
        
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
    

    


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    mainwindow = MainWindowForm()
    mainwindow.show()
    sys.exit(app.exec_())

