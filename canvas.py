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

SELECTED_COLOUR = QtGui.QColor(255, 0, 0, 127)
UNSELECTED_COLOUR = QtGui.QColor(0, 0, 255, 127)

class Canvas(QtGui.QGraphicsView):


    def __init__(self):
        super(Canvas, self).__init__()
        self.scene = Scene(QtCore.QRectF(self.contentsRect()))
        self.setScene(self.scene)
        self.setAcceptDrops(True)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.customContextMenuRequest)
        self.selectedItem = None # If None, selected item refers to Canvas.

    @QtCore.pyqtSlot(QtCore.QPoint)
    def customContextMenuRequest(self, qpoint):
        print("Custom Context Menu")
        menu = QtGui.QMenu()
        action1 = menu.addAction("Delete")
        menu.addSeparator()
        action2 = menu.addAction("Properties")
        action1.triggered.connect(lambda: self.menuRemove(qpoint))
        action2.triggered.connect(self.properties)

        print(self.mapToGlobal(qpoint))
        menu.exec_(self.mapToGlobal(qpoint))


    def dropEvent(self, event):
        pos = event.pos()
        # Lock to Grid
        remain = int(pos.x() / GRID_WIDTH)
        x = remain * GRID_WIDTH
        remain = int(pos.y() / GRID_HEIGHT)
        y = remain * GRID_HEIGHT
        rect = drawables.objrepr.Repr(scene=self.scene, x=x, y=y,
                                      brush=SELECTED_COLOUR)

        if not self.selectedItem is None:
            self.selectedItem.setBrush(UNSELECTED_COLOUR)
            self.updateSceneRect(self.selectedItem.boundingRect())

        self.selectedItem = rect

    def dragEnterEvent(self, event):
        print("Drag Enter Event {}".format(event))
        event.accept()

    def mousePressEvent(self, event):
        '''
        :Description:
            Adds border to a drawable item to notify user of what is currently
            selected. Only one thing can be selected at a time. Upon start
            of application, the entire canvas should be "selected".

            NOTE: Keyboard shortcuts should be applicable to selected items.
            Example: Typing a word will search all the current items and select
            the closest thing, or bring up a list of items that can be selected
            via keyboard.
            Ctrl or Alt + key, or delete/home/end/pgup/pgdn keys should be able
            to affect droppables too. TODO.
        '''
        print("Mouse Press Event")
        item = self.scene.itemAt(event.pos())
        if not item is None and not item == self.selectedItem:
            item.setBrush(SELECTED_COLOUR)
            self.selectedItem.setBrush(UNSELECTED_COLOUR)
            self.selectedItem = item

    def mouseReleaseEvent(self, event):
        pass
        #print(event.pos())
        #print(self.contentsRect())

    def resizeEvent(self, event):
        self.scene.setSceneRect(QtCore.QRectF(QtCore.QPointF(0, 0),
                                              QtCore.QSizeF(event.size())))

    @QtCore.pyqtSlot()
    def properties(self):
        print("Hello World")

    @QtCore.pyqtSlot()
    def menuRemove(self, point, success=print):
        item = self.scene.itemAt(point)
        if not item is None:
            self.scene.removeItem(item)
            success(item)


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
        NOTE: currently unused until it can be in its own layer and be statically drawn
              onto the scene.
        '''
        width = int(self.sceneRect().width())
        height = int(self.sceneRect().height())

        for n in range(0, height, GRID_HEIGHT): # 0 - 822
            self.addLine(0, n, width, n, pen=self.gridPen)

        for n in range(0, width, GRID_WIDTH): # 0 - 596
            self.addLine(n, 0, n, height, pen=self.gridPen)
