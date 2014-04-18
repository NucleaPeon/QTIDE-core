'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui, QtCore

class Canvas(QtGui.QGraphicsView):
    
    def __init__(self):
        super(Canvas, self).__init__()
        self.setAcceptDrops(True)
        
    def dropEvent(self, event):
        print(event.mimeData().text())
        
    def dragEnterEvent(self, event):
        event.accept()