#!/usr/bin/env python3
"""ADUP UI module"""

# Import widgets for PyQt5 (on 2 lines for ease of reading)
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QComboBox, QCheckBox, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout, QMainWindow

class AdupUI(QMainWindow):
    """ADUP View (GUI)."""
    def __init__(self, controller):
        #View initializer
        super().__init__()
        self._controller = controller
        # Set some main window's properties
        self.setWindowTitle('User Creator')
        self.setFixedSize(400, 500)
        self.general_layout = QVBoxLayout()
        # Set the central widget which is the parent for the rest of the gui components
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        #Create the main form
        self._create_main_form()
        self._create_checkboxes()
        self._create_buttons()
        self.detect_button_click()
        self.detect_text_changes()
        self.set_company_combobox()
        self.detect_combobox_change()
        self.set_ou_combobox()

    def _create_main_form(self):
        #Create the main form
        self.main_form_layout = QFormLayout()
        #Create the form's widgets
        self.fn_line_edit = QLineEdit()
        self.sn_line_edit = QLineEdit()
        self.dn_line_edit = QLineEdit()
        self.pre2k_line_edit = QLineEdit()
        self.uln_line_edit = QLineEdit()
        self.company_combobox = QComboBox()
        self.dept_combobox = QComboBox()
        self.job_title_combobox = QComboBox()
        self.mngr_line_edit = QLineEdit()
        self.emp_no_line_edit = QLineEdit()
        self.psswd_line_edit = QLineEdit()
        #Set the password to hidden
        self.psswd_line_edit.setEchoMode(QLineEdit.Password)
        self.org_unit_combobox = QComboBox()
        self.get_org_unit_btn = QPushButton()
        #Add widgets to form
        self.main_form_layout.addRow(QLabel("First Name: *"), self.fn_line_edit)
        self.main_form_layout.addRow(QLabel("Surname: *"), self.sn_line_edit)
        self.main_form_layout.addRow(QLabel("Display Name: *"), self.dn_line_edit)
        self.main_form_layout.addRow(QLabel("Pre 2k Logon Name: *"), self.pre2k_line_edit)
        self.main_form_layout.addRow(QLabel("User Logon Name: *"), self.uln_line_edit)
        self.main_form_layout.addRow(QLabel("Company: *"), self.company_combobox)
        self.main_form_layout.addRow(QLabel("Department: *"), self.dept_combobox)
        self.main_form_layout.addRow(QLabel("Job Title: *"), self.job_title_combobox)
        self.main_form_layout.addRow(QLabel("Manager: *"), self.mngr_line_edit)
        self.main_form_layout.addRow(QLabel("Employee Number:"), self.emp_no_line_edit)
        self.main_form_layout.addRow(QLabel("Password: *"), self.psswd_line_edit)
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
        self.check_duplicate_btn = QPushButton("Check for duplicates", self)
        self.check_duplicate_line_edit = QLineEdit()
        self.check_duplicate_line_edit.setReadOnly(True)
        self.create_powershell_btn = QPushButton("Create Powershell Cmd", self)
        self.create_powershell_command_result_line_edit = QLineEdit()
        self.create_powershell_command_result_line_edit.setReadOnly(True)
        self.create_user_btn = QPushButton("Create User", self)
        #button set to disabled until conditions are met
        self.create_user_btn.setEnabled(False)
        #Add buttons to form
        self.buttons_layout.addRow(self.check_duplicate_btn, self.check_duplicate_line_edit)
        self.buttons_layout.addRow(self.create_powershell_btn, self.create_powershell_command_result_line_edit)
        self.buttons_layout.addRow(self.create_user_btn)
        #Add to the main layout
        self.general_layout.addLayout(self.buttons_layout)

    def detect_combobox_change(self):
        """Detect changes to the comboboxes and call a function sending combobox text"""
        self.company_combobox.currentTextChanged.connect(self.set_department_combobox)
        self.dept_combobox.currentTextChanged.connect(self.set_job_combobox)

    def set_company_combobox(self):
        """Set the company combobox values"""
        companies = self._controller.get_companies()
        self.company_combobox.addItems(companies)

    def set_department_combobox(self):
        """Set the department combobox values"""
        #Clears the box if the user changes their mind
        self.dept_combobox.clear()
        departments = self._controller.get_next_combo_element(self.company_combobox.currentText(), 'company')
        self.dept_combobox.addItems(departments)

    def set_job_combobox(self):
        """Set the Job combobox values"""
        #Clears the box if the user changes their mind
        self.job_title_combobox.clear()
        jobs = self._controller.get_next_combo_element(self.dept_combobox.currentText(), 'department', self.company_combobox.currentText(), self.dept_combobox.currentIndex())
        self.job_title_combobox.addItems(jobs)

    def set_ou_combobox(self):
        try:
            self.org_unit_combobox.addItems(self._controller.get_ou_structure())
        except Exception as e:
            print("Unable to query OU structure")
            print(e)

    def detect_text_changes(self):
        """Detect when a form item changes and call the mandatory field check"""
        self.fn_line_edit.textChanged.connect(self.check_mandatory_fields)
        self.sn_line_edit.textChanged.connect(self.check_mandatory_fields)
        self.dn_line_edit.textChanged.connect(self.check_mandatory_fields)
        self.pre2k_line_edit.textChanged.connect(self.check_mandatory_fields)
        self.uln_line_edit.textChanged.connect(self.check_mandatory_fields)
        self.company_combobox.currentIndexChanged.connect(self.check_mandatory_fields)
        self.dept_combobox.currentIndexChanged.connect(self.check_mandatory_fields)
        self.job_title_combobox.currentIndexChanged.connect(self.check_mandatory_fields)
        self.mngr_line_edit.textChanged.connect(self.check_mandatory_fields)
        self.psswd_line_edit.textChanged.connect(self.check_mandatory_fields)
        self.org_unit_combobox.currentIndexChanged.connect(self.check_mandatory_fields)

    def detect_button_click(self):
        """Detects when a button is pressed and sends to controller"""
        self.create_powershell_btn.clicked.connect(self.create_powershell_command)
        self.create_user_btn.clicked.connect(self.create_user)
        self.check_duplicate_btn.clicked.connect(self.check_duplicate_usr)

    def check_mandatory_fields(self):
        """Detects if the mandatory fields are filled, if not the create user button will be deactivated"""
        if(self.fn_line_edit.text() != '' and self.sn_line_edit.text() and self.dn_line_edit.text() != '' and self.pre2k_line_edit.text() != '' and self.uln_line_edit.text() != '' and  self.company_combobox.currentText != '' and self.dept_combobox.currentText != '' and self.job_title_combobox.currentText != '' and self.mngr_line_edit.text() != '' and self.psswd_line_edit.text() != '' and self.org_unit_combobox.currentText != ''):
            self.create_user_btn.setEnabled(True)
        else:
            self.create_user_btn.setEnabled(False)

    def check_duplicate_usr(self):
        """Checks if the filled in SAM name matches an existing user"""
        user_exists = self._controller.usr_exist_check(self.pre2k_line_edit.text(), self.uln_line_edit.text())

        if user_exists == True:
            self.check_duplicate_line_edit.setText("User already exists")
        else:
            self.check_duplicate_line_edit.setText("User does not exist")

    def create_powershell_command(self):
        """Create the user creation Powershell command"""        
        command = self._controller.create_user_command(self.fn_line_edit.text(), self.sn_line_edit.text(), self.dn_line_edit.text(), self.pre2k_line_edit.text(), self.uln_line_edit.text(), self.company_combobox.currentText(), self.dept_combobox.currentText(), self.job_title_combobox.currentText(), self.mngr_line_edit.text(), self.org_unit_combobox.currentText(), self.psswd_line_edit.text(), self.change_psswd.checkState(), self.psswd_no_expire.checkState())
        
        #Clear line edit before filling it 
        self.create_powershell_command_result_line_edit.clear()
        self.create_powershell_command_result_line_edit.setText(command)

    def create_user(self):
        """Get create user command and create user"""
        command = self._controller.create_user_command(self.fn_line_edit.text(), self.sn_line_edit.text(), self.dn_line_edit.text(), self.pre2k_line_edit.text(), self.uln_line_edit.text(), self.company_combobox.currentText(), self.dept_combobox.currentText(), self.job_title_combobox.currentText(), self.mngr_line_edit.text(), self.psswd_line_edit.text(), self.org_unit_combobox.currentText())

        try:
            self._controller.create_user(command)
        except Exception as e:
            print(e)
