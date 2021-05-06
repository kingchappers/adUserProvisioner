#!/usr/bin/env python3
"""ADUP model Module"""

import json

class AdupMdl:
    """ADUP Model Class"""
    def read_json_file(self, json_file):
        """Read the json file"""
        with open(json_file, 'r') as json_file:
            json_data = json.load(json_file)
    