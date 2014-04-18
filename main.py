#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:Author:
    - Daniel Kettle

"""
import os
import sys
import window
import argparse

def main():
    '''
    '''
    # Add to path
    # Until software can be properly installed onto the OS and paths become
    # predictable, assume running from top level directory
    sys.path.append(os.path.join(os.getcwd(),
                              os.path.dirname(__file__)))

    from PyQt4 import QtGui
    app = QtGui.QApplication(sys.argv)
    app.aboutToQuit.connect(shutdown)
    win = window.Window()
    win.show()
    
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec_())
    
def shutdown():
    print("Shutdown")


###
### Start parsing arguments from the command line here:
###
if __name__ == "__main__":
    # Argument Parsing
    parser = argparse.ArgumentParser(description='QT-Based Drag and Drop IDE')
    args = parser.parse_args(sys.argv[1:])
    
    main()
