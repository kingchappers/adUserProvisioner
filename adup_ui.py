#!/usr/bin/env python3
"""adup ui module"""

# Import QApplication and the required widgets from PyQt5.QtWidgets
# This works even with pylint moaning
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QFormLayout, QLabel, QComboBox

from PyQt5.QtCore import Qt

class AdupUI(QMainWindow):
    """adupUI's View (GUI)."""
    def __init__(self):
        #View initializer
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('User Creator')
        self.setFixedSize(300, 500)
        self.general_layout = QHBoxLayout()
        # Set the central widget which is the parent for the rest of the gui components
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        # Create the main form
        self._create_main_form()
        #self._create_buttons()

    def _create_main_form(self):
        # Create the main form
        self.main_form_layout = QFormLayout()
        #Create the form's widgets
        self.fn_line_edit = QLineEdit()
        self.sn_line_edit = QLineEdit()
        self.dn_line_edit = QLineEdit()
        self.uln_line_edit = QLineEdit()
        self.upn_line_edit = QLineEdit()
        self.office_combobox = QComboBox()
        self.dept_combobox = QComboBox()
        self.role_combobox = QComboBox()
        self.mngr_line_edit = QLineEdit()
        self.emp_no_line_edit = QLineEdit()
        self.psswd_line_edit = QLineEdit()
        self.org_unit_combobox = QComboBox()
        #set the password to hidden
        self.psswd_line_edit.setEchoMode(QLineEdit.Password)
        # Set create the actual form
        self.main_form_layout.addRow(QLabel("First Name:"), self.fn_line_edit)
        self.main_form_layout.addRow(QLabel("Surname:"), self.sn_line_edit)
        self.main_form_layout.addRow(QLabel("Display Name:"), self.dn_line_edit)
        self.main_form_layout.addRow(QLabel("User Logon Name:"), self.uln_line_edit)
        self.main_form_layout.addRow(QLabel("User Principal Name:"), self.upn_line_edit)
        self.main_form_layout.addRow(QLabel("Office:"), self.office_combobox)
        self.main_form_layout.addRow(QLabel("Department:"), self.dept_combobox)
        self.main_form_layout.addRow(QLabel("Role:"), self.role_combobox)
        self.main_form_layout.addRow(QLabel("Manager:"), self.mngr_line_edit)
        self.main_form_layout.addRow(QLabel("Employee Number:"), self.emp_no_line_edit)
        self.main_form_layout.addRow(QLabel("Password:"), self.psswd_line_edit)
        self.main_form_layout.addRow(QLabel("Organisational Unit:"), self.org_unit_combobox)
        #Add this form layout to the main layout
        self.general_layout.addLayout(self.main_form_layout)

    def _create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }
        # Create the buttons and add them to the grid layout
        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(40, 40)
            buttons_layout.addWidget(self.buttons[btn_text], pos[0], pos[1])
        # Add buttons_layout to the general layout
        self.general_layout.addLayout(buttons_layout)

    def set_displaytext(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        """Get display's text."""
        return self.display.text()

    def clear_display(self):
        """Clear the display."""
        self.set_displaytext('')