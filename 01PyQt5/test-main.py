import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from test import *

class MyWindow(QMainWindow,Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.exitAction.triggered.connect(self.onExitTriggered)
        self.copyAction.triggered.connect(self.onCopyTriggered)
        self.pasteAction.triggered.connect(self.onPasteTriggered)
        self.cutAction.triggered.connect(self.onCutTriggered)
        self.openAction.triggered.connect(self.onOpenTriggered)
        self.viewMsg.triggered.connect(self.onViewTriggered)

    def onViewTriggered(self):


    def onExitTriggered(self):
        QMessageBox.information(self, "Information", "Exit action triggered")
        pass

    def onCopyTriggered(self):
        QMessageBox.information(self, "Information", "Copy action triggered")
        pass

    def onPasteTriggered(self):
        QMessageBox.information(self, "Information", "Paste action triggered")
        pass

    def onCutTriggered(self):
        QMessageBox.information(self, "Information", "Cut action triggered")
        pass

    def onOpenTriggered(self):
        QMessageBox.information(self, "Information", "Open action triggered")
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())