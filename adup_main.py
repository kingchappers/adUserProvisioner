#!/usr/bin/env python3
"""ADUP Main module."""

import sys
from PyQt5.QtWidgets import QApplication

from adup_ctrl import AdupCtrl
from adup_ui import AdupUI
from adup_mdl import AdupMdl

def main():
    """ADUP Main function."""
    # Create an instance of QApplication
    adup = QApplication(sys.argv)
    #Instanciate Model
    model = AdupMdl()
    #Instanciate Controller
    controller = AdupCtrl(model=model)
    #Instanciate View
    view = AdupUI(controller = controller)
    #Show the GUI
    view.show()
    
    
    # Execute the main loop
    sys.exit(adup.exec_())

if __name__ == '__main__':
    main()
    