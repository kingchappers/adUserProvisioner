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
        #self._signal_listener()
        self.set_company_combobox()
        self.detect_combobox_change()
        self.detect_button_click()

    def _create_main_form(self):
        #Create the main form
        self.main_form_layout = QFormLayout()
        #Create the form's widgets
        self.fn_line_edit = QLineEdit()
        self.sn_line_edit = QLineEdit()
        self.dn_line_edit = QLineEdit()
        self.uln_line_edit = QLineEdit()
        self.upn_line_edit = QLineEdit()
        self.company_combobox = QComboBox()
        #self.company_combobox.setPlaceholderText("Select an item...")
        self.dept_combobox = QComboBox()
        #self.dept_combobox.addItem("Select an item...")
        self.job_title_combobox = QComboBox()
        #self.job_title_combobox.addItem("Select an item...")
        self.mngr_line_edit = QLineEdit()
        self.emp_no_line_edit = QLineEdit()
        self.psswd_line_edit = QLineEdit()
        #Set the password to hidden
        self.psswd_line_edit.setEchoMode(QLineEdit.Password)
        self.org_unit_combobox = QComboBox()
        #Add widgets to form
        self.main_form_layout.addRow(QLabel("First Name:"), self.fn_line_edit)
        self.main_form_layout.addRow(QLabel("Surname:"), self.sn_line_edit)
        self.main_form_layout.addRow(QLabel("Display Name:"), self.dn_line_edit)
        self.main_form_layout.addRow(QLabel("User Logon Name:"), self.uln_line_edit)
        self.main_form_layout.addRow(QLabel("User Principal Name:"), self.upn_line_edit)
        self.main_form_layout.addRow(QLabel("Company:"), self.company_combobox)
        self.main_form_layout.addRow(QLabel("Department:"), self.dept_combobox)
        self.main_form_layout.addRow(QLabel("Job Title:"), self.job_title_combobox)
        self.main_form_layout.addRow(QLabel("Manager:"), self.mngr_line_edit)
        self.main_form_layout.addRow(QLabel("Employee Number:"), self.emp_no_line_edit)
        self.main_form_layout.addRow(QLabel("Password:"), self.psswd_line_edit)
        self.main_form_layout.addRow(QLabel("Oraganisational Unit:"), self.org_unit_combobox)
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
        #self.company_combobox.setCurrentIndex(-1)

    def set_department_combobox(self):
        """Set the department combobox values"""
        #Clears the box if the user changes their mind
        self.dept_combobox.clear()
        departments = self._controller.get_next_combo_element(self.company_combobox.currentText(), 'company')
        self.dept_combobox.addItems(departments)
        #self.dept_combobox.setCurrentIndex(-1)

    def set_job_combobox(self):
        """Set the Job combobox values"""
        #Clears the box if the user changes their mind
        self.job_title_combobox.clear()
        jobs = self._controller.get_next_combo_element(self.dept_combobox.currentText(), 'department', self.company_combobox.currentText(), self.dept_combobox.currentIndex())
        self.job_title_combobox.addItems(jobs)

    def detect_button_click(self):
        """Detects when a button is pressed and sends to controller"""
        #self.create_powershell_btn.clicked.connect(self._controller.create_user_command(self.fn_line_edit.text, self.sn_line_edit.text, self.dn_line_edit.text, self.uln_line_edit.text, self.upn_line_edit.text, self.company_combobox.currentText, self.dept_combobox.currentText, self.job_title_combobox.currentText, self.mngr_line_edit.text, self.psswd_line_edit.text, self.org_unit_combobox.currentText, True))
        self.create_powershell_btn.clicked.connect(self.create_powershell_command)

    def create_powershell_command(self):
        """Create the user creation Powershell command"""        
        command = self._controller.create_user_command(self.fn_line_edit.text(), self.sn_line_edit.text(), self.dn_line_edit.text(), self.uln_line_edit.text(), self.upn_line_edit.text(), self.company_combobox.currentText(), self.dept_combobox.currentText(), self.job_title_combobox.currentText(), self.mngr_line_edit.text(), self.psswd_line_edit.text(), self.org_unit_combobox.currentText())

        #Clear line edit before filling it 
        self.create_powershell_command_result_line_edit.clear()

        #self.create_powershell_command_result_line_edit.setText(self.fn_line_edit.text())

        self.create_powershell_command_result_line_edit.setText(command)
