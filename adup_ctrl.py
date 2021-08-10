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

    def create_user_command(self, firstname, surname, displayname, user_logon_name, user_principal_name, company, department, job_title, manager, password, org_unit, pass_to_subprocess):
        """Create the command to create a new user in powershell"""
        print("hello")