'''
:Author:
    - Daniel Kettle
'''

from PyQt4 import QtGui
import dock.droppable
import languages.langread

import os
import json

class LanguageDock(QtGui.QDockWidget):

    def __init__(self):
        super(LanguageDock, self).__init__()
        self.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.setWindowTitle(QtGui.QApplication.translate(
            "self", "Language", None, QtGui.QApplication.UnicodeUTF8))
        self.widget = QtGui.QWidget()
        self.setWidget(self.widget)
        self.layout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom)
        self.widget.setLayout(self.layout)
        self.pixmap = QtGui.QPixmap(os.path.join(os.getcwd(),
                              os.path.dirname(__file__), 'folder-development.png'))

        # Load test set of usable objects
        language = languages.langread.read_languages()

        def lang_qt_objects(l, layout=self.layout):
            '''
            Appends a series of QtGui objects to the layout,
            based on contents of l (language) input

            :Parameters:
                - l: language array from read_languages()
            '''
            langwidget = QtGui.QWidget()
            langwidget.setLayout(QtGui.QVBoxLayout())
            layout.addWidget(QtGui.QLabel(l.get('Language') + ":"))
            for obj in l.get('Objects'):
                entry = QtGui.QWidget()
                entry.setLayout(QtGui.QHBoxLayout())
                d = dock.droppable.Droppable(pixmap = self.pixmap)
                if obj.get('type', None) is None:
                    continue

                # Add json data as a string for entire object
                print(obj)
                d.mime.setText(json.dumps(obj))
                d.mime.setImageData(self.pixmap)
                d.setPixmap(self.pixmap)
                entry.layout().addWidget(d)
                entry.layout().addWidget(QtGui.QLabel(obj.get('type')))
                entry.layout().insertStretch(-1)
                langwidget.layout().addWidget(entry)
            layout.addWidget(langwidget)

        for lang in language:
            lang_qt_objects(lang)

        self.layout.insertStretch(-1)

