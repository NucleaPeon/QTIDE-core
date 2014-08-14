'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui, QtCore
import dock.language
import canvas

class Window(QtGui.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__()
        self.setWindowTitle(
            QtGui.QApplication.translate("QT-Based Drag and Drop IDE",
                "QT-Based Drag and Drop IDE",
                None, QtGui.QApplication.UnicodeUTF8))
        self.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        #        qrect = QtGui.QApplication.desktop().screen().rect()
        self.resize(1000, 600)
        self.canvas = canvas.Canvas()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setCentralWidget(self.canvas)
        self.languagedock = dock.language.LanguageDock()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.languagedock)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.canvas.customContextMenuRequest)

        # self.setWindowIcon(QtGui.QIcon('web.png'))
