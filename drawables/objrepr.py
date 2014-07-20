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
     on 64-bit systems. (not recommended in practice) )
     
'''

class Repr(QtGui.QGraphicsRectItem):
    
    def __init__(self, x=0, y=0, w=100, h=60, pen=None, brush=None):
        super().__init__(x, y, w, h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine) if pen is None else pen
        self.brush = brush
    
    