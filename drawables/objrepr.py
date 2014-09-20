from PyQt4 import QtGui, QtCore

'''
Object Representation Drawing
    Based on QGraphicsScene drawRect()

:Author:
    Daniel Kettle

:Description:
    objrepr.py is the python class that dynamically generates the rectangle
    images for dnd functionality. Instead of statically creating a class
    per object (ex: Namespace/Variable/Class) per Language (Python, c++, etc),
    the language xml should define core functionality found in these objects.

    A variable tends to have a handle (name) and a value.
    If "foo" = "bar", foo is the string and "bar" is the string value.
    The xml could define a variable's contents as:
        <objecttype type="Variable">
            <SingleField>
                <handle repr="Name">
                    <type>string</type>
                </handle>
                <value repr="Value">
                    <type>any</type>
                </value>
            </SingleField>
        </objecttype>

        # TODO: Define all primitive types

    The variable drawing would consist of a rectangle with two text fields:
        Name and Value

    We can extend functionality around language limitations (for example) by
    adding <maxlength>50</maxlength> or similar to the name, or to the value
    (ex: limit to max string length to 32-bit system string length even while
     on 64-bit systems. )

'''

class Repr(QtGui.QGraphicsRectItem):

    def __init__(self, *args, x=0, y=0, w=100, h=60, brush=None, name='Foo Bar',
                  **kwargs):
        super().__init__(x, y, w, h, scene=kwargs.get('scene', None))
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 127),
                                  style=QtCore.Qt.SolidPattern) if brush is None else brush
        self.setBrush(self.brush)
        self.setToolTip(name)

