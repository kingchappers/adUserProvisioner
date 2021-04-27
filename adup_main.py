#!/usr/bin/env python3
"""ADUP Main module."""

import sys
from PyQt5.QtWidgets import QApplication

from adup_ctrl import AdupCtrl
from adup_ui import AdupUI

def main():
    """ADUP Main function."""
    # Create an instance of QApplication
    adup = QApplication(sys.argv)
    # Show the calculator's GUI
    view = AdupUI()
    view.show()
    # Create instances of the model and the controller
    #model = evaluateExpression
    AdupCtrl(view=view)
    # Execute the calculator's main loop
    sys.exit(adup.exec_())

if __name__ == '__main__':
    main()
    