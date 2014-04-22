'''
:Author:
    - Daniel Kettle
'''

import os
from lxml import etree
from PyQt4 import QtGui, QtCore

LANG_DIR = os.path.join(os.getcwd(), os.path.dirname(__file__))

def read_languages():
    found_langs = []
    lang = None
    for d in os.listdir(LANG_DIR):
        if d[-4:].lower() == ".xml":
            lang = read_file(os.path.join(LANG_DIR, d))
            if not lang is None:
                found_langs.append(lang)
            
    return found_langs
            
def read_file(filename):
    '''
    Reads the xml file containing the language specification
    
    :Description:
        (Detailed Description here)
        
    :Parameters:
        - filename: string path to file to read
    
    '''        
    doc = etree.parse(filename)
    if not doc.getroot().tag == "Language" or doc.getroot() is None:
        return None
    # Get <Language>
    node = doc.getroot()
    language = {'Language': node.get('name')}
    # Get <Object>s
    node = node.findall('Object')
    nodes = []
    language['Objects'] = []
    obj = {} # Reuse dictionary instead of re-creating each time
    for o in node:
        # obj will default to {'type' : 'str'}, where str is a language element (Class, etc)
        obj = dict(o.attrib)
        
        for tag in ['accept', 'refuse', 'restrict']:
            subelement = o.find(tag)
            if not subelement is None:
                types = subelement.findall('objecttype')
                obj[tag] = [t.get('type') for t in types]
                
        #obj['accepts'] = str(o.find('accept'))
        #obj['refuses'] = str(o.find('refuse'))
        #obj['restrict']  = str(o.find('restrict'))
        language['Objects'].append(obj)
        
    return language