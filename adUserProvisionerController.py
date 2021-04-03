#!/usr/bin/env python3

from userInterface.userCreationMainWindow import Ui_MainWindow

#Controller class
class adUserCreationCtrl:
    #PyCalc Controller class.
    def __init__(self, model, view):
        #Controller initializer.
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()