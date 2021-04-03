# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userCreationUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_userCreationWindow(object):
    def setupUi(self, userCreationWindow):
        if not userCreationWindow.objectName():
            userCreationWindow.setObjectName(u"userCreationWindow")
        userCreationWindow.resize(547, 553)
        userCreationWindow.setToolTipDuration(-7)
        self.actionExit = QAction(userCreationWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setEnabled(True)
        self.centralwidget = QWidget(userCreationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 30, 281, 321))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.firstNameLabel = QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.firstNameLabel)

        self.firstNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.firstNameLineEdit)

        self.surnameLabel = QLabel(self.formLayoutWidget)
        self.surnameLabel.setObjectName(u"surnameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.surnameLabel)

        self.surnameLineEdit = QLineEdit(self.formLayoutWidget)
        self.surnameLineEdit.setObjectName(u"surnameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.surnameLineEdit)

        self.displayNameLabel = QLabel(self.formLayoutWidget)
        self.displayNameLabel.setObjectName(u"displayNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.displayNameLabel)

        self.displayNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.displayNameLineEdit.setObjectName(u"displayNameLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.displayNameLineEdit)

        self.logonNameLabel = QLabel(self.formLayoutWidget)
        self.logonNameLabel.setObjectName(u"logonNameLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.logonNameLabel)

        self.logonNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.logonNameLineEdit.setObjectName(u"logonNameLineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.logonNameLineEdit)

        self.principalNameLabel = QLabel(self.formLayoutWidget)
        self.principalNameLabel.setObjectName(u"principalNameLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.principalNameLabel)

        self.principalNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.principalNameLineEdit.setObjectName(u"principalNameLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.principalNameLineEdit)

        self.officeLabel = QLabel(self.formLayoutWidget)
        self.officeLabel.setObjectName(u"officeLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.officeLabel)

        self.officeComboBox = QComboBox(self.formLayoutWidget)
        self.officeComboBox.setObjectName(u"officeComboBox")
        self.officeComboBox.setDuplicatesEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.officeComboBox)

        self.departmentLabel = QLabel(self.formLayoutWidget)
        self.departmentLabel.setObjectName(u"departmentLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.departmentLabel)

        self.departmentComboBox = QComboBox(self.formLayoutWidget)
        self.departmentComboBox.setObjectName(u"departmentComboBox")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.departmentComboBox)

        self.roleLabel = QLabel(self.formLayoutWidget)
        self.roleLabel.setObjectName(u"roleLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.roleLabel)

        self.roleComboBox = QComboBox(self.formLayoutWidget)
        self.roleComboBox.setObjectName(u"roleComboBox")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.roleComboBox)

        self.managerLabel = QLabel(self.formLayoutWidget)
        self.managerLabel.setObjectName(u"managerLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.managerLabel)

        self.managerLineEdit = QLineEdit(self.formLayoutWidget)
        self.managerLineEdit.setObjectName(u"managerLineEdit")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.managerLineEdit)

        self.employeeNumberLabel = QLabel(self.formLayoutWidget)
        self.employeeNumberLabel.setObjectName(u"employeeNumberLabel")
        self.employeeNumberLabel.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.employeeNumberLabel)

        self.employeeNumberLineEdit = QLineEdit(self.formLayoutWidget)
        self.employeeNumberLineEdit.setObjectName(u"employeeNumberLineEdit")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.employeeNumberLineEdit)

        self.organisationalUnitLabel = QLabel(self.formLayoutWidget)
        self.organisationalUnitLabel.setObjectName(u"organisationalUnitLabel")
        self.organisationalUnitLabel.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.organisationalUnitLabel)

        self.organisationalUnitComboBox = QComboBox(self.formLayoutWidget)
        self.organisationalUnitComboBox.setObjectName(u"organisationalUnitComboBox")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.organisationalUnitComboBox)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 350, 281, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.changePasswordCheckBox = QCheckBox(self.verticalLayoutWidget)
        self.changePasswordCheckBox.setObjectName(u"changePasswordCheckBox")
        self.changePasswordCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.changePasswordCheckBox)

        self.passwordExpiresCheckBox = QCheckBox(self.verticalLayoutWidget)
        self.passwordExpiresCheckBox.setObjectName(u"passwordExpiresCheckBox")
        self.passwordExpiresCheckBox.setAutoFillBackground(False)
        self.passwordExpiresCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.passwordExpiresCheckBox)

        self.powershellCommandToolButton = QToolButton(self.centralwidget)
        self.powershellCommandToolButton.setObjectName(u"powershellCommandToolButton")
        self.powershellCommandToolButton.setGeometry(QRect(30, 460, 91, 41))
        self.powershellCommandToolButton.setAutoRaise(False)
        self.createUserToolButton = QToolButton(self.centralwidget)
        self.createUserToolButton.setObjectName(u"createUserToolButton")
        self.createUserToolButton.setGeometry(QRect(30, 410, 91, 41))
        self.createUserToolButton.setAutoRaise(False)
        self.powershellCommandLineEdit = QLineEdit(self.centralwidget)
        self.powershellCommandLineEdit.setObjectName(u"powershellCommandLineEdit")
        self.powershellCommandLineEdit.setEnabled(True)
        self.powershellCommandLineEdit.setGeometry(QRect(130, 470, 181, 23))
        self.powershellCommandLineEdit.setReadOnly(True)
        self.availableDisplayNameLabel = QLabel(self.centralwidget)
        self.availableDisplayNameLabel.setObjectName(u"availableDisplayNameLabel")
        self.availableDisplayNameLabel.setGeometry(QRect(310, 90, 57, 15))
        self.availableLogonLabel = QLabel(self.centralwidget)
        self.availableLogonLabel.setObjectName(u"availableLogonLabel")
        self.availableLogonLabel.setGeometry(QRect(310, 120, 57, 15))
        self.availablePrincipalNameLabel = QLabel(self.centralwidget)
        self.availablePrincipalNameLabel.setObjectName(u"availablePrincipalNameLabel")
        self.availablePrincipalNameLabel.setGeometry(QRect(310, 150, 57, 15))
        self.availableEmployeeNumberLabel = QLabel(self.centralwidget)
        self.availableEmployeeNumberLabel.setObjectName(u"availableEmployeeNumberLabel")
        self.availableEmployeeNumberLabel.setGeometry(QRect(310, 290, 57, 15))
        userCreationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(userCreationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 547, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        userCreationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(userCreationWindow)
        self.statusbar.setObjectName(u"statusbar")
        userCreationWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(userCreationWindow)

        QMetaObject.connectSlotsByName(userCreationWindow)
    # setupUi

    def retranslateUi(self, userCreationWindow):
        userCreationWindow.setWindowTitle(QCoreApplication.translate("userCreationWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("userCreationWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("userCreationWindow", u"Exit Program", None))
#endif // QT_CONFIG(tooltip)
        self.firstNameLabel.setText(QCoreApplication.translate("userCreationWindow", u"First Name", None))
        self.surnameLabel.setText(QCoreApplication.translate("userCreationWindow", u"Surname", None))
        self.displayNameLabel.setText(QCoreApplication.translate("userCreationWindow", u"Display Name", None))
        self.logonNameLabel.setText(QCoreApplication.translate("userCreationWindow", u"User Logon Name", None))
        self.principalNameLabel.setText(QCoreApplication.translate("userCreationWindow", u"User Principal Name", None))
        self.officeLabel.setText(QCoreApplication.translate("userCreationWindow", u"Office", None))
        self.officeComboBox.setCurrentText("")
        self.officeComboBox.setPlaceholderText("")
        self.departmentLabel.setText(QCoreApplication.translate("userCreationWindow", u"Department", None))
        self.roleLabel.setText(QCoreApplication.translate("userCreationWindow", u"Role", None))
        self.managerLabel.setText(QCoreApplication.translate("userCreationWindow", u"Manager", None))
        self.employeeNumberLabel.setText(QCoreApplication.translate("userCreationWindow", u"Employee Number", None))
        self.organisationalUnitLabel.setText(QCoreApplication.translate("userCreationWindow", u"Organisational Unit", None))
        self.changePasswordCheckBox.setText(QCoreApplication.translate("userCreationWindow", u"Change Password at Next Logon", None))
        self.passwordExpiresCheckBox.setText(QCoreApplication.translate("userCreationWindow", u"Password Never Expires", None))
        self.powershellCommandToolButton.setText(QCoreApplication.translate("userCreationWindow", u"Powershell\n"
"Command", None))
        self.createUserToolButton.setText(QCoreApplication.translate("userCreationWindow", u"Create User", None))
        self.availableDisplayNameLabel.setText(QCoreApplication.translate("userCreationWindow", u"TextLabel", None))
        self.availableLogonLabel.setText(QCoreApplication.translate("userCreationWindow", u"TextLabel", None))
        self.availablePrincipalNameLabel.setText(QCoreApplication.translate("userCreationWindow", u"TextLabel", None))
        self.availableEmployeeNumberLabel.setText(QCoreApplication.translate("userCreationWindow", u"TextLabel", None))
        self.menuFile.setTitle(QCoreApplication.translate("userCreationWindow", u"&File", None))
    # retranslateUi

