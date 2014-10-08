'''
:Author:
    - Daniel Kettle

:TODO:
    - Grid must be an overlay on top of scene and not added TO the scene if possible
    - ItemGroups: Drawables should be in groups: a namespace creates a group from which all classes exist.
                  Classes contain a group of methods and one of variables.
                  Methods contain an optional group of variables. etc.
'''

from PyQt4 import QtGui, QtCore
import drawables.objrepr

GRID_HEIGHT = 20
GRID_WIDTH = 20

ITEM_HEIGHT = 60
ITEM_WIDTH = 100

class Canvas(QtGui.QGraphicsView):

    def __init__(self):
        super(Canvas, self).__init__()
        self.scene = QtGui.QGraphicsScene(QtCore.QRectF(0, 0, 1000, 600))
        self.setScene(self.scene)
        self.setAcceptDrops(True)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.customContextMenuRequest)
        self.setInteractive(True)

    @QtCore.pyqtSlot(QtCore.QPoint)
    def customContextMenuRequest(self, qpoint):
        menu = QtGui.QMenu()
        action1 = menu.addAction("Delete")
        menu.addSeparator()
        action2 = menu.addAction("Properties")
        action1.triggered.connect(lambda: self.menuRemove(qpoint))
        action2.triggered.connect(self.properties)
        menu.exec_(self.mapToGlobal(qpoint))

    @QtCore.pyqtSlot()
    def properties(self):
        print("Hello World")

    @QtCore.pyqtSlot()
    def menuRemove(self, point, success=print):
        item = self.scene.itemAt(point)
        if not item is None:
            self.scene.removeItem(item)
            success(item)

    def dropEvent(self, event):
        pos = event.pos()
        # Lock to Grid
        remain = int(pos.x() / GRID_WIDTH)
        x = remain * GRID_WIDTH
        remain = int(pos.y() / GRID_HEIGHT)
        y = remain * GRID_HEIGHT
        #rect = drawables.objrepr.Repr(event.mimeData().text(),
                                      #QtCore.QRectF(pos.x(), pos.y(),
                                                   #ITEM_WIDTH, ITEM_HEIGHT),
                                      #scene=self.scene,
                                      #brush=SELECTED_COLOUR)
        rect = self.scene.addRect(x, y, 100, 60, brush=QtGui.QColor(0, 0, 255, 127))
        rect.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        rect.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)

    def dragEnterEvent(self, event):
        print("Drag Enter Event {}".format(event))
        event.accept()

    def resizeEvent(self, event):
        self.scene.setSceneRect(QtCore.QRectF(QtCore.QPointF(0, 0),
                                              QtCore.QSizeF(event.size())))

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