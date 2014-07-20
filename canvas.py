'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui, QtCore
import drawables.objrepr

class Canvas(QtGui.QGraphicsView):
    
    def __init__(self):
        super(Canvas, self).__init__()
        self.scene = Scene(QtCore.QRectF(self.contentsRect()))
        self.setScene(self.scene)
        self.setAcceptDrops(True)
        
        
    def dropEvent(self, event):
        print("Drop Event {}".format(event.mimeData().text()))
        # Create Object
        rect = drawables.objrepr.Repr()
        self.scene.addItem(rect)
        print(rect)
        
    def dragEnterEvent(self, event):
        print("Drag Enter Event {}".format(event))
        event.accept()
        
    def mouseReleaseEvent(self, event):
        print(event.pos())
        print(self.contentsRect())
        
    def resizeEvent(self, event):
        self.scene.setSceneRect(QtCore.QRectF(QtCore.QPointF(0, 0),
                                              QtCore.QSizeF(event.size())))
        self.scene.clear()
        self.scene.drawGrid()
        
        
class Scene(QtGui.QGraphicsScene):
    
    #TODO: set font
    
    def __init__(self, rect):
        super(Scene, self).__init__(rect)
        self.gridPen = QtGui.QPen(QtCore.Qt.gray, 1, QtCore.Qt.SolidLine)
        
    def dropEvent(self, event):
        print("Drop Event {}".format(event))
        
    def dragEnterEvent(self, event):
        print("Drag Enter Event {}".format(event))
        
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

    def drawGrid(self):
        '''
        Recreates a grid onto the scene.
        '''
        width = int(self.sceneRect().width())
        height = int(self.sceneRect().height())
        
        for n in range(0, height, 20): # 0 - 822
            self.addLine(0, n, width, n, pen=self.gridPen)
        for n in range(0, width, 20): # 0 - 596
            self.addLine(n, 0, n, height, pen=self.gridPen)
        