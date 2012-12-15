
# These are only needed for Python v2 but are harmless for Python v3.
import sip
import this
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)


from PyQt4 import QtCore, QtGui
from magmasoft.censocath.view.ui_mainwindow import Ui_MainWindow
from magmasoft.censocath.model.sqlmodel import FamiliaModel
from magmasoft.censocath.util.connection import Connection



class MainWindowForm(QtGui.QMainWindow):
    __familiaModel = None
    
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__initDatabase()
        self.ui.actionSalir.triggered.connect(self.on_salir_triggered)
        pass
    

    
    @QtCore.pyqtSlot(bool)
    def on_salir_triggered(self):
        """mb = QtGui.QMessageBox()
        mb.setText("una prueba")
        mb.exec_()"""
        QtGui.QApplication.quit()
        pass
    
    
    def __initDatabase(self):
        Connection.createConnection()
        self.__familiaModel = FamiliaModel( )
        self.ui.tableView.setModel(self.__familiaModel)
        pass


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindowForm()
    mainwindow.show()
    sys.exit(app.exec_())

