
# These are only needed for Python v2 but are harmless for Python v3.
import sip
# import this
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)


from PyQt4 import QtCore, QtGui
from magmasoft.censocath.view.ui_mainwindow import Ui_MainWindow
from magmasoft.censocath.view.ui_encuestadialog import Ui_WzrdEncuesta
from magmasoft.censocath.model.sqlmodel import FamiliaModel
from magmasoft.censocath.util.connection import Connection




class EncuestaDialogForm(QtGui.QWizard):
    
    def __init__(self, parent=None):
        super(EncuestaDialogForm, self).__init__(parent)
        self.ui = Ui_WzrdEncuesta()
        self.ui.setupUi(self)
        pass


class MainWindowForm(QtGui.QMainWindow):
    __familiaModel = None
    __wzrdEncuesta = None
    
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionSalir.triggered.connect(self.on_salir_triggered)
        self.ui.actionNueva_Encuesta.triggered.connect(self.on_new_encuesta_triggered)
        
        
        self.__wzrdEncuesta = EncuestaDialogForm(self)
        
        self.__initDatabase()
        
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
        self.__familiaModel = FamiliaModel( )
        self.ui.tblVwEncuestas.setModel(self.__familiaModel)
        pass
    
    


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindowForm()
    mainwindow.show()
    sys.exit(app.exec_())

