'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui, QtCore
import drawables.objrepr

GRID_HEIGHT = 20
GRID_WIDTH = 20

class Canvas(QtGui.QGraphicsView):

    def __init__(self):
        super(Canvas, self).__init__()
        #self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.customContextMenuRequested.connect(self.customContextMenuRequest)
        self.scene = Scene(QtCore.QRectF(self.contentsRect()))
        self.setScene(self.scene)
        self.setAcceptDrops(True)

    @QtCore.pyqtSlot(QtCore.QPoint)
    def customContextMenuRequest(self, qpoint):
        menu = QtGui.QMenu()
        action1 = menu.addAction("Item 1")
        action2 = menu.addAction("Item 2")
        action1.triggered.connect(self.helloWorld)
        #menu.connect(action1.SIGNAL("triggered()"),
        #             self.SLOT("helloWorld()"))

        #menu.connect(action2.SIGNAL("triggered()"),
        #             #self.SLOT("helloWorld()"))

        menu.exec_(qpoint)


    def dropEvent(self, event):
        pos = event.pos()
        # Lock to Grid
        remain = int(pos.x() / GRID_WIDTH)
        x = remain * GRID_WIDTH
        print(x)
        remain = int(pos.y() / GRID_HEIGHT)
        y = remain * GRID_HEIGHT
        print(y)
        rect = drawables.objrepr.Repr(x=x,
                                      y=y)
        self.scene.addItem(rect)

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

    @QtCore.pyqtSlot()
    def helloWorld(self):
        print("Hello World")


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

        for n in range(0, height, GRID_HEIGHT): # 0 - 822
            self.addLine(0, n, width, n, pen=self.gridPen)
        for n in range(0, width, GRID_WIDTH): # 0 - 596
            self.addLine(n, 0, n, height, pen=self.gridPen)
