from PyQt4 import QtCore, QtGui

from ui_mainwindow import Ui_MainWindow


class MainWindowForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowForm, self).__init__(parent)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

    #@QtCore.pyqtSlot(int)
    #def on_inputSpinBox1_valueChanged(self, value):
    #    self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox2.value()))

    #@QtCore.pyqtSlot(int)
    #def on_inputSpinBox2_valueChanged(self, value):
    #    self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox1.value()))


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindowForm()
    mainwindow.show()
    sys.exit(app.exec_())

