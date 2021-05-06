#!/usr/bin/env python3
"""ADUP controller module."""

#Controller class
class AdupCtrl:
    """ADUP Controller Class."""
    def __init__(self, model, view):
        #Controller initializer.
        #self._evaluate = model
        self._view = view
        self._model = model
        # Connect signals and slots
        #self._connectSignals()
    
    def populate_view_dropdowns(self):
        """Populate the view's dropdown options"""
        config_file_location = './config/config.json'
        json_data = self._model.read_json_file(config_file_location)
        print(json_data['company'][2]['department'][0]['roles'][0])
        #print(json_data['company'].keys())
