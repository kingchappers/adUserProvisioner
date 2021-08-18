#!/usr/bin/env python3
"""ADUP model Module"""

import json
import subprocess

class AdupMdl:
    """ADUP Model Class"""
    def read_json_file(self, json_file_location):
        """Read the json file"""
        with open(json_file_location, 'r') as json_file:
            json_data = json.load(json_file)

        #by deafault the json_data is of dict (dictionary) type when imported, but will be processed later on
        return json_data

    def run_usr_creation_powershell_command(self, cmd):
        """Run a Powershell Command using subprocess"""
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True, check=True)
        return completed

    def query_usr_manager(self, manager_name):
        """Query AD to see if the entered manager exists"""

    def get_ou_structure(self):
        """Get the AD structure, this is used to populate the OU dropdown""" 
        get_ou_structure_command = "Get-ADOrganizationalUnit -Filter * -Properties CanonicalName | select-object CanonicalName"