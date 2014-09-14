'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui, QtCore

class Droppable(QtGui.QLabel):

    def __init__(self, pixmap = None):
        super(Droppable, self).__init__()
        self.mime = QtCore.QMimeData()
        self.pixmap = pixmap

    def mousePressEvent(self, event):
        mime = QtCore.QMimeData()
        mime.setText(self.mime.text())
        hotSpot = event.pos()
        mime.setData("application/x-hotspot", str(hotSpot.x()))

        # Create a pixmap of size of self
        if self.pixmap is None:
            self.pixmap = QtGui.QPixmap(self.size())
            
        drag = QtGui.QDrag(self)
        drag.setMimeData(mime)
        drag.setPixmap(self.pixmap)
        drag.setHotSpot(hotSpot)

        dropAction = drag.exec_(QtCore.Qt.CopyAction|QtCore.Qt.MoveAction, QtCore.Qt.CopyAction)