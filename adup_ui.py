#!/usr/bin/env python3
"""adup ui module"""

# Import widgets for PyQt5 (on 2 lines for ease of reading)
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QComboBox, QCheckBox, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout, QMainWindow

class AdupUI(QMainWindow):
    """adupUI's View (GUI)."""
    def __init__(self):
        #View initializer
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('User Creator')
        self.setFixedSize(300, 500)
        self.general_layout = QVBoxLayout()
        # Set the central widget which is the parent for the rest of the gui components
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        #Create the main form
        self._create_main_form()
        self._create_checkboxes()
        self._create_buttons()

    def _create_main_form(self):
        #Create the main form
        self.main_form_layout = QFormLayout()
        #Create the form's widgets
        self.fn_line_edit = QLineEdit()
        self.sn_line_edit = QLineEdit()
        self.dn_line_edit = QLineEdit()
        self.uln_line_edit = QLineEdit()
        self.upn_line_edit = QLineEdit()
        self.job_title_combobox = QComboBox()
        self.dept_combobox = QComboBox()
        self.company_combobox = QComboBox()
        self.mngr_line_edit = QLineEdit()
        self.emp_no_line_edit = QLineEdit()
        self.psswd_line_edit = QLineEdit()
        self.org_unit_combobox = QComboBox()
        #Set the password to hidden
        self.psswd_line_edit.setEchoMode(QLineEdit.Password)
        #Add widgets to form
        self.main_form_layout.addRow(QLabel("First Name:"), self.fn_line_edit)
        self.main_form_layout.addRow(QLabel("Surname:"), self.sn_line_edit)
        self.main_form_layout.addRow(QLabel("Display Name:"), self.dn_line_edit)
        self.main_form_layout.addRow(QLabel("User Logon Name:"), self.uln_line_edit)
        self.main_form_layout.addRow(QLabel("User Principal Name:"), self.upn_line_edit)
        self.main_form_layout.addRow(QLabel("Job Title:"), self.job_title_combobox)
        self.main_form_layout.addRow(QLabel("Department:"), self.dept_combobox)
        self.main_form_layout.addRow(QLabel("Company:"), self.company_combobox)
        self.main_form_layout.addRow(QLabel("Manager:"), self.mngr_line_edit)
        self.main_form_layout.addRow(QLabel("Employee Number:"), self.emp_no_line_edit)
        self.main_form_layout.addRow(QLabel("Password:"), self.psswd_line_edit)
        self.main_form_layout.addRow(QLabel("Organisational Unit:"), self.org_unit_combobox)
        #Add this form layout to the main layout
        self.general_layout.addLayout(self.main_form_layout)

    def _create_checkboxes(self):
        self.checkbox_layout = QVBoxLayout()
        #Create checkbox widgets
        self.change_psswd = QCheckBox("Change Password at Next Logon")
        self.psswd_no_expire = QCheckBox("Password Never Expires")
        #set checkboxes to checked
        self.change_psswd.setChecked(True)
        self.psswd_no_expire.setChecked(True)
        #Add checkboxes to form
        self.checkbox_layout.addWidget(self.change_psswd)
        self.checkbox_layout.addWidget(self.psswd_no_expire)
        #Add to the main layout
        self.general_layout.addLayout(self.checkbox_layout)

    def _create_buttons(self):
        self.buttons_layout = QFormLayout()
        #Create the widgets
        self.check_duplicate_btn = QPushButton("Check for duplicates")
        self.check_duplicate_line_edit = QLineEdit()
        self.check_duplicate_line_edit.setReadOnly(True)
        self.create_powershell_btn = QPushButton("Create Powershell Command")
        self.create_powershell_command_result_line_edit = QLineEdit()
        self.create_powershell_command_result_line_edit.setReadOnly(True)
        self.create_user_btn = QPushButton("Create User")
        #Add buttons to form
        self.buttons_layout.addRow(self.check_duplicate_btn, self.check_duplicate_line_edit)
        self.buttons_layout.addRow(self.create_powershell_btn, self.create_powershell_command_result_line_edit)
        self.buttons_layout.addRow(self.create_user_btn)
        #Add to the main layout
        self.general_layout.addLayout(self.buttons_layout)

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
