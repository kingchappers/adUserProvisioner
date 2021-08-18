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
        get_ou_structure_command = "$OUs = Get-ADOrganizationalUnit -Filter * \n $OUs.DistinguishedName"
        #Run the powershell command 
        cmd_raw_output = subprocess.run(["powershell", "-Command", get_ou_structure_command], capture_output=True, check=True)
        #convert the powershell command result to a string
        cmd_output_as_string = cmd_raw_output.stdout.decode('utf-8').rstrip()
        #convert the powershell command result to a list split by the \r\n characters
        cmd_output_list = cmd_output_as_string.split("\r\n")

        return cmd_output_list
