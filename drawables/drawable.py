from PyQt4 import QtGui, QtCore

'''
:Description:
    Base class for drawable items, contains methods that are required to
    reimplement if extending canvas objects, such as container or item.

    For ease of use, we will only concern ourselves with QGraphicsRectItems,
    any odd shapes (circles) should fit inside a rect boundary.
    This may be revisited at a later date.
'''

class Drawable(QtGui.QGraphicsRectItem):

    def __init__(self, dimensions, scene, brush=None):
        super().__init__(dimensions, scene=scene)
        self.dimensions = dimensions
        self.brush = QtGui.QBrush(QtGui.QColor(0, 0, 255, 127),
                                  style=QtCore.Qt.SolidPattern) \
                                  if brush is None else brush
        self.setBrush(self.brush)
        #self.setPen()
        self.components = []

    def consolidate(self):
        '''
        :Description:
            Redraw every component in as space-efficient a manner as possible.
            Call this when an item is added or removed.
        '''
        pass

    def select(self):
        self.setBrush(QtGui.QBrush(QtGui.QColor(255, 0, 0, 127),
                                  style=QtCore.Qt.SolidPattern))

    def deselect(self):
        self.setBrush(self.brush)