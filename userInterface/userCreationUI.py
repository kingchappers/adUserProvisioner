#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userCreationUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QMainWindow

class Ui_userCreationUIWindow(object):
    def setupUi(self, userCreationUIWindow):
        userCreationUIWindow.setObjectName("userCreationUIWindow")
        userCreationUIWindow.resize(547, 553)
        userCreationUIWindow.setToolTipDuration(-7)
        self.centralwidget = QtWidgets.QWidget(userCreationUIWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 281, 321))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.surnameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.surnameLabel.setObjectName("surnameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surnameLabel)
        self.surnameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.surnameLineEdit.setObjectName("surnameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surnameLineEdit)
        self.displayNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.displayNameLabel.setObjectName("displayNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.displayNameLabel)
        self.displayNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.displayNameLineEdit.setObjectName("displayNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.displayNameLineEdit)
        self.logonNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.logonNameLabel.setObjectName("logonNameLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.logonNameLabel)
        self.logonNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.logonNameLineEdit.setObjectName("logonNameLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.logonNameLineEdit)
        self.principalNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.principalNameLabel.setObjectName("principalNameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.principalNameLabel)
        self.principalNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.principalNameLineEdit.setObjectName("principalNameLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.principalNameLineEdit)
        self.officeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.officeLabel.setObjectName("officeLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.officeLabel)
        self.officeComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.officeComboBox.setCurrentText("")
        self.officeComboBox.setPlaceholderText("")
        self.officeComboBox.setDuplicatesEnabled(False)
        self.officeComboBox.setObjectName("officeComboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.officeComboBox)
        self.departmentLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName("departmentLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.departmentLabel)
        self.departmentComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName("departmentComboBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.departmentComboBox)
        self.roleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.roleLabel.setObjectName("roleLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.roleLabel)
        self.roleComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.roleComboBox.setObjectName("roleComboBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.roleComboBox)
        self.managerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.managerLabel.setObjectName("managerLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.managerLabel)
        self.managerLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.managerLineEdit.setObjectName("managerLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.managerLineEdit)
        self.employeeNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.employeeNumberLabel.setTextFormat(QtCore.Qt.AutoText)
        self.employeeNumberLabel.setObjectName("employeeNumberLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.employeeNumberLabel)
        self.employeeNumberLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.employeeNumberLineEdit.setObjectName("employeeNumberLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.employeeNumberLineEdit)
        self.organisationalUnitLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.organisationalUnitLabel.setTextFormat(QtCore.Qt.AutoText)
        self.organisationalUnitLabel.setObjectName("organisationalUnitLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.organisationalUnitLabel)
        self.organisationalUnitComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.organisationalUnitComboBox.setObjectName("organisationalUnitComboBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.organisationalUnitComboBox)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 350, 281, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.changePasswordCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.changePasswordCheckBox.setChecked(True)
        self.changePasswordCheckBox.setObjectName("changePasswordCheckBox")
        self.verticalLayout.addWidget(self.changePasswordCheckBox)
        self.passwordExpiresCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.passwordExpiresCheckBox.setAutoFillBackground(False)
        self.passwordExpiresCheckBox.setChecked(True)
        self.passwordExpiresCheckBox.setObjectName("passwordExpiresCheckBox")
        self.verticalLayout.addWidget(self.passwordExpiresCheckBox)
        self.powershellCommandToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.powershellCommandToolButton.setGeometry(QtCore.QRect(30, 460, 91, 41))
        self.powershellCommandToolButton.setAutoRaise(False)
        self.powershellCommandToolButton.setObjectName("powershellCommandToolButton")
        self.createUserToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.createUserToolButton.setGeometry(QtCore.QRect(30, 410, 91, 41))
        self.createUserToolButton.setAutoRaise(False)
        self.createUserToolButton.setObjectName("createUserToolButton")
        self.powershellCommandLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.powershellCommandLineEdit.setEnabled(True)
        self.powershellCommandLineEdit.setGeometry(QtCore.QRect(130, 470, 181, 23))
        self.powershellCommandLineEdit.setReadOnly(True)
        self.powershellCommandLineEdit.setObjectName("powershellCommandLineEdit")
        self.availableDisplayNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.availableDisplayNameLabel.setGeometry(QtCore.QRect(310, 90, 57, 15))
        self.availableDisplayNameLabel.setObjectName("availableDisplayNameLabel")
        self.availableLogonLabel = QtWidgets.QLabel(self.centralwidget)
        self.availableLogonLabel.setGeometry(QtCore.QRect(310, 120, 57, 15))
        self.availableLogonLabel.setObjectName("availableLogonLabel")
        self.availablePrincipalNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.availablePrincipalNameLabel.setGeometry(QtCore.QRect(310, 150, 57, 15))
        self.availablePrincipalNameLabel.setObjectName("availablePrincipalNameLabel")
        self.availableEmployeeNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.availableEmployeeNumberLabel.setGeometry(QtCore.QRect(310, 290, 57, 15))
        self.availableEmployeeNumberLabel.setObjectName("availableEmployeeNumberLabel")
        userCreationUIWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(userCreationUIWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        userCreationUIWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(userCreationUIWindow)
        self.statusbar.setObjectName("statusbar")
        userCreationUIWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(userCreationUIWindow)
        self.actionExit.setEnabled(True)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(userCreationUIWindow)
        QtCore.QMetaObject.connectSlotsByName(userCreationUIWindow)

    def retranslateUi(self, userCreationUIWindow):
        _translate = QtCore.QCoreApplication.translate
        userCreationUIWindow.setWindowTitle(_translate("userCreationUIWindow", "MainWindow"))
        self.firstNameLabel.setText(_translate("userCreationUIWindow", "First Name"))
        self.surnameLabel.setText(_translate("userCreationUIWindow", "Surname"))
        self.displayNameLabel.setText(_translate("userCreationUIWindow", "Display Name"))
        self.logonNameLabel.setText(_translate("userCreationUIWindow", "User Logon Name"))
        self.principalNameLabel.setText(_translate("userCreationUIWindow", "User Principal Name"))
        self.officeLabel.setText(_translate("userCreationUIWindow", "Office"))
        self.departmentLabel.setText(_translate("userCreationUIWindow", "Department"))
        self.roleLabel.setText(_translate("userCreationUIWindow", "Role"))
        self.managerLabel.setText(_translate("userCreationUIWindow", "Manager"))
        self.employeeNumberLabel.setText(_translate("userCreationUIWindow", "Employee Number"))
        self.organisationalUnitLabel.setText(_translate("userCreationUIWindow", "Organisational Unit"))
        self.changePasswordCheckBox.setText(_translate("userCreationUIWindow", "Change Password at Next Logon"))
        self.passwordExpiresCheckBox.setText(_translate("userCreationUIWindow", "Password Never Expires"))
        self.powershellCommandToolButton.setText(_translate("userCreationUIWindow", "Powershell\n"
"Command"))
        self.createUserToolButton.setText(_translate("userCreationUIWindow", "Create User"))
        self.availableDisplayNameLabel.setText(_translate("userCreationUIWindow", "TextLabel"))
        self.availableLogonLabel.setText(_translate("userCreationUIWindow", "TextLabel"))
        self.availablePrincipalNameLabel.setText(_translate("userCreationUIWindow", "TextLabel"))
        self.availableEmployeeNumberLabel.setText(_translate("userCreationUIWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("userCreationUIWindow", "&File"))
        self.actionExit.setText(_translate("userCreationUIWindow", "Exit"))
        self.actionExit.setToolTip(_translate("userCreationUIWindow", "Exit Program"))
