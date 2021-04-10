#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication

from userInterface import userCreationUI
from adUserProvisionerCtrl import adUserCreationCtrl

def main():
    #Main function.
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = userCreationUI.Ui_userCreationUIWindow()
    view.show()
    # Create instances of the model and the controller
    #model = evaluateExpression
    adUserCreationCtrl(view=view)
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())