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
    def get_next_combo_element(self, combobox_text, combo_name, boxText="test", boxIndex=0):
        """Select the next values of the combobox based on the selection of another"""
        config_file_location = './config/config.json'
        json_data = self._model.read_json_file(config_file_location)

        if combo_name == 'company':
            department_list = list()
            for i in json_data[combobox_text]:
                #print(i)
                #print(i['deptName'])
                #print(list(i.values())[0])
                department_list.append(list(i.values())[0])
                #print(type(list(i.values())[0]))
                #return "poop"

            #print(department_list)
            return department_list
        elif combo_name == 'department':
            job_title_list = list()
            print(type(json_data[boxText][boxIndex]))
            print("_________________________")
            #print(json_data[boxText][boxIndex]['roles'][0])
            for i in json_data[boxText][boxIndex]['roles']:
                job_title_list.append(i)
                #print(i)
                #print(json_data[boxText][boxIndex]['roles'][i])
            #print(job_title_list)
            return job_title_list
        #    for i in json_data[boxText][1]["deptName"]:
        #        department_list.append(list(i))
        #        print(department_list)
        #print(json_data[combobox_text]['deptName'])
        #print(combobox_text)
        #print(json_data.items())
