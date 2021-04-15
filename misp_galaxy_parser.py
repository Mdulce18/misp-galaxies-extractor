# This class has to take the json file, then format the data and return the community identifiers.

import logging


class community_extractor():
    def __init__(self):
        self.misp_galaxy_json_link = 'https://github.com/MISP/misp-galaxy/blob/main/clusters/threat-actor.json'
        self.community_identifiers_list = None

    def parse_community_identifiers_json(self):
        json = '123'
        return json

    def create_list(self,name):
        name1 = name 
        identifiers_list = []
        self.community_identifiers_list= name1

    def get_community_identifiers(self):
        return self.community_identifiers_list
