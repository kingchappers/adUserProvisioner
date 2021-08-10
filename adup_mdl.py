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

    def run_powershell_command(self, cmd):
        """Run a Powershell Command using subprocess"""
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True, check=True)
        return completed
        