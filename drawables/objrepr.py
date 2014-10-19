from PyQt4 import QtGui, QtCore
import drawables.drawable

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

class Repr(drawables.drawable.Drawable):
    '''
    :Description:
        This object represents a structural component of a computer language

        It is a square that contains rules on how to behave with other structural
        components as well as appearance on the scene and view.
    '''

    def __init__(self, obj_repr, rect, *args, brush=None, name=None,
                  **kwargs):
        super().__init__(rect, kwargs.get('scene', None))
        self.data = obj_repr # dict with data
        self.name = obj_repr.get('type') if name is None else name
        self.setToolTip(self.name)
        self.setAcceptDrops(True)

    def request_name(self):
        text, ok = QtGui.QInputDialog.getText(self, "Enter {} Name".format(self.obj_repr),
                                              "Name:")
        return text

