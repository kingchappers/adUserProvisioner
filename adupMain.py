#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication

from adupCtrl import adUserCreationCtrl
from adupUI import adupUI

def main():
    #Main function.
    # Create an instance of QApplication
    adup = QApplication(sys.argv)
    # Show the calculator's GUI
    view = adupUI()
    view.show()
    # Create instances of the model and the controller
    #model = evaluateExpression
    adUserCreationCtrl(view=view)
    # Execute the calculator's main loop
    sys.exit(adup.exec_())

if __name__ == '__main__':
    main()