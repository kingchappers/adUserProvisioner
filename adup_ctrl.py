#!/usr/bin/env python3
"""ADUP controller module."""

#Controller class
class AdupCtrl:
    """ADUP Controller Class."""
    def __init__(self, model):
        #Controller initializer.
        self._model = model
        
    def get_company_combobox(self):
        """Populate the view's dropdown options"""
        config_file_location = './config/config.json'
        json_data = self._model.read_json_file(config_file_location)

        return json_data.keys()
