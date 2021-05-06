#!/usr/bin/env python3
"""ADUP controller module."""

#Controller class
class AdupCtrl:
    """ADUP Controller Class."""
    def __init__(self, model, view):
        #Controller initializer.
        self._view = view
        self._model = model
        # Connect signals and slots
        #self._connectSignals()
        self.populate_view_dropdowns()
        
    def populate_view_dropdowns(self):
        """Populate the view's dropdown options"""
        config_file_location = './config/config.json'
        json_data = self._model.read_json_file(config_file_location)
        print(json_data)
        print(type(json_data))
        print("_______________________________")
       
        for key in json_data.keys():
            self._view.set_company_combobox(key)
            print(key)
            print(type(key))
        print("_______________________________")

        for item in json_data['Holdings'][0].items():
            print(item)
            print(type(item))
        print("_______________________________")

        for i in json_data['Holdings'][0]['roles']:
            print(i)
        print("_______________________________")

        print(json_data['Holdings'][1])
        print(type(json_data['Holdings'][1]))
