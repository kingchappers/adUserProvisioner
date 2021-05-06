#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication

from adup_ctrl import AdupCtrl
from adup_ui import AdupUI
from adup_mdl import AdupMdl

adup = QApplication(sys.argv)
# Show the calculator's GUI
view = AdupUI()
# Create instances of the model and the controller
model = AdupMdl()
ctrl = AdupCtrl(model=model, view=view)
ctrl.populate_view_dropdowns()
