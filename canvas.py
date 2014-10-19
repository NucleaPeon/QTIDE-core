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
import json

GRID_HEIGHT = 20
GRID_WIDTH = 20

ITEM_HEIGHT = 60
ITEM_WIDTH = 100

class Canvas(QtGui.QGraphicsView):

    def __init__(self):
        super(Canvas, self).__init__()
        '''
        when dragging an item around, this holds the current stack of items
        below the cursor
        '''
        self.hovered_items = None
        '''
        In order to deselect items once the mouse cursor leaves them, this
        caches which items were last found. A comparison is made against them
        and this is only reassigned if the hovered items are different.
        '''
        self.last_discovered_items = []
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
        rect = drawables.objrepr.Repr(json.loads(event.mimeData().text()),
                                      QtCore.QRectF(x, y,
                                                   ITEM_WIDTH, ITEM_HEIGHT),
                                      scene=self.scene,
                                      brush=QtGui.QColor(0, 0, 255, 127))
        #rect = self.scene.addRect(x, y, 100, 60, brush=QtGui.QColor(0, 0, 255, 127))
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

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        # If there is > 1 item at this event position, call select() on item
        # (Example: two items are touching. Clicking one remains deselected
        #  until you drag it out of the scope of first item then hover again)
        if len(self.items(event.pos())) > 1:
            for item in self.last_discovered_items:
                    item.select()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        # Get items below cursor
        self.hovered_items = self.items(event.pos())
        # Manage items if multiple items are found
        if len(self.hovered_items) > 1:
            # Check if items under cursor are different from last event
            if self.last_discovered_items != self.hovered_items[1:]:
                self.last_discovered_items = self.hovered_items[1:]
                for item in self.last_discovered_items:
                    item.select()

        else:
            # Deselect all items
            for ldi in self.last_discovered_items:
                ldi.deselect()
                self.last_discovered_items = []

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        # If we are hovering over the same items that are selected
        if len(self.hovered_items) > 1 and self.hovered_items[1:] == self.last_discovered_items:
            print("COMBINE!")

        for ldi in self.last_discovered_items:
            ldi.deselect()
