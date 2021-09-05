#!/usr/bin/env python3
"""ADUP controller module."""

#Controller class
class AdupCtrl:
    """ADUP Controller Class."""
    def __init__(self, model):
        #Controller initializer.
        self._model = model

    def get_companies(self):
        """Populate the view's dropdown options"""
        config_file_location = './config/config.json'
        json_data = self._model.read_json_file(config_file_location)
        print(type(json_data.keys()))
        return json_data.keys()

    #the x=y function arguments indicate an optional argument, if the argument isn't sent the y value is the default
    def get_next_combo_element(self, combobox_text, combo_name, box_text="test", box_index=0):
        """Select the next values of the combobox based on the selection of another"""
        config_file_location = './config/config.json'
        json_data = self._model.read_json_file(config_file_location)

        if combo_name == 'company':
            department_list = list()
            for i in json_data[combobox_text]:
                department_list.append(list(i.values())[0])

            return department_list

        elif combo_name == 'department':
            job_title_list = list()
            for i in json_data[box_text][box_index]['roles']:
                job_title_list.append(i)

            return job_title_list

    def create_user_command(self, firstname, surname, displayname, user_logon_name, user_principal_name, company, department, job_title, manager, org_unit, password, change_psswd, expire_psswd):
        """Create the command to create a new user in powershell"""
        create_usr_cmd = f"New-ADUser -Name '{displayname}' -GivenName '{firstname}' -Surname '{surname}' -SamAccountName '{user_logon_name}' -UserPrincipalName '{user_principal_name}' -Company '{company}' -Department '{department}' -Title '{job_title}' -Path '{org_unit}' -AccountPassword (ConvertTo-SecureString -AsPlainText '{password}' -Force) -Enabled $true -ChangePasswordAtLogon {change_psswd} -PasswordNeverExpires {expire_psswd}"

        #Manager must be an existing user so I need to create a search function for this user

        return create_usr_cmd

    def create_user(self, command):
        self._model.create_user_in_powershell(command)

    def get_ou_structure(self):
        """Get the OU structure"""
        ou_structure = self._model.query_ad_ou_structure()
        return ou_structure
