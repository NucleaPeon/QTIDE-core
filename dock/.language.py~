'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui
import dock.droppable

import os

class LanguageDock(QtGui.QDockWidget):
    
    def __init__(self):
        super(LanguageDock, self).__init__()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.widget = QtGui.QWidget()
        self.setWidget(self.widget)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.pixmap = QtGui.QPixmap(os.path.join(os.getcwd(),
                              os.path.dirname(__file__), 'folder-development.png'))
        self.droppables = QtGui.QWidget()
        self.droppables.setLayout(QtGui.QVBoxLayout())
        self.c = dock.droppable.Droppable(pixmap = self.pixmap)
        self.c.mime.setText("Class")
        self.c.mime.setImageData(self.pixmap)
        self.c.setPixmap(self.pixmap)
        self.droppables.layout().addWidget(self.c)
        self.layout.addWidget(self.droppables)
        self.layout.insertStretch(-1)
        
        