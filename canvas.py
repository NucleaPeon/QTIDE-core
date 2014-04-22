'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui, QtCore

class Canvas(QtGui.QGraphicsView):
    
    def __init__(self):
        super(Canvas, self).__init__(Scene())
        self.setAcceptDrops(True)
        
    def dropEvent(self, event):
        print(event.mimeData().text())
        
    def dragEnterEvent(self, event):
        event.accept()
        
        
class Scene(QtGui.QGraphicsScene):
    
    def __init__(self):
        super(Scene, self).__init__()
        
    def dropEvent(self, event):
        print(event)
        
    def dragEnterEvent(self, event):
        print(event)
        
    def dragMoveEvent(self, event):
        '''
        :Description:
            Required method to enable drag and drop functionality from a 
            scene object. (Works with QGraphicsView but not QGraphicsScene)
            
        :See:
            - http://qt-project.org/forums/viewthread/3156
        '''
        source = event.source()
        if source:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
