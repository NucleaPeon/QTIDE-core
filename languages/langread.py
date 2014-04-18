'''
:Author:
    - Daniel Kettle
'''

import os
from lxml import etree
from PyQt4 import QtGui, QtCore

LANG_DIR = os.path.join(os.getcwd(), os.path.dirname(__file__))

def read_languages():
    for d in os.listdir(LANG_DIR):
        if d[-4:].lower() == ".xml":
            read_file(os.path.join(LANG_DIR, d))
            
def read_file(filename):
    doc = etree.parse(filename)
    print(doc)