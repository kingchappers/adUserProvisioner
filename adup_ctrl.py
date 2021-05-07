#!/usr/bin/env python3
"""ADUP controller module."""

#Controller class
class AdupCtrl:
    """ADUP Controller Class."""
    def __init__(self, model):
        #Controller initializer.
        self._model = model
        # Connect signals and slots
        self._connect_signals()
        
    def get_company_combobox(self):
        """Populate the view's dropdown options"""
        config_file_location = './config/config.json'
        json_data = self._model.read_json_file(config_file_location)

        print(json_data.keys())
        return json_data.keys()

        #Grab the top level keys from the json file and use them to populate the company combobox
        #for key in json_data.keys():
         #   self._view.set_company_combobox(key)

        #Printing a bunch of things for testing and understanding
        #print(json_data)
        #print(type(json_data))
        #print("_______________________________")
       
        #for key in json_data.keys():
            #print(key)
            #print(type(key))
        #print("_______________________________")

        #for item in json_data['Holdings'][0].items():
            #print(item)
            #print(type(item))
        #print("_______________________________")

        #for i in json_data['Holdings'][0]['roles']:
            #print(i)
        #print("_______________________________")

        #print(json_data['Holdings'][1])
        #print(type(json_data['Holdings'][1]))

    def _connect_signals(self):
        #self._view.signal_listener()
        #if self._view.company_combobox.currentIndexChanged:
            #print("item changed")

        #print(self._view.company_combobox.currentText())

        #self._view.company_combobox.addItem('turd')
        #self._view.create_user_btn.clicked.connect(moreprint_shit)
        #self._view.create_user_btn.clicked.connect(self._print_shit)
        #self._view.create_user_btn.clicked.connect(self._model.print_shit2)
        #self._view.create_user_btn.clicked.connect(self._view.successful_button3)
        #self._view.company_combobox.textHighlighted.connect(self._print_shit)
        print("butts")
        #self.print_shit()


    def _print_shit(self):
        print("poopCtrl")
        #self._model.print_shit2()

def moreprint_shit():
        print("poopfuncinfile")

