#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication

from userInterface.userCreationMainWindow import Ui_MainWindow
from adUserProvisionerController import adUserCreationCtrl
from adUserProvisioner.userInterface.userCreationUI import Ui_userCreationWindow

def main():
    #Main function.
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    adUserCreationCtrl(model=model, view=view)
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())