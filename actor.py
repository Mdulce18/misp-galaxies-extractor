# This class has to take the json file, then format the data and return the community identifiers.

import logging
import requests
import json


class Actor():  # Actor
    def __init__(self, actor_number, misp_galaxy_json_link=None):
        if not misp_galaxy_json_link:
            self.misp_galaxy_json_link = 'https://raw.githubusercontent.com/MISP/misp-galaxy/main/clusters/threat-actor.json'
            self.community_identifiers_list = []
            self.actor_number = actor_number
        else:
            self.misp_galaxy_json_link = misp_galaxy_json_link
            self.community_identifiers_list = []
            self.actor_number = actor_number

    def parse_community_identifiers_json(self):
        # parse json from raw github
        try:
            resp = requests.get(self.misp_galaxy_json_link)
        except requests.exceptions.MissingSchema:
            logging.error("Invalid URL Error")
            return None

        data = json.loads(resp.text)
        try:
            # parse main actor name
            actor_name = data['values'][self.actor_number]['value']
        except IndexError:
            logging.error("Actor Index Error")
            return None

        try:
            # parse community identifiers
            community_identifiers_raw = data['values'][self.actor_number]['meta']['synonyms']
            community_identifiers_raw.append(actor_name)
        except KeyError:
            logging.error("Actor without Aliases")
            return None
        return community_identifiers_raw


    def format_data(self, clist):
        # format data and delete duplicates
        try:
            lowered_list = [x.lower() for x in clist]
            no_space_list = [x.replace(' ', '_') for x in lowered_list]
        except TypeError:
            logging.error('Input data Error')
            return None
        # maintain apt withouth _ | add conditions if necessary
        for name in no_space_list:
            if ('apt_' in name) or ('advanced_persistent_threat_' in name):
                no_space_list.remove(name)
            # save values with _
            elif '_' in name:
                name1 = name.replace('_', '')
                if name1 in no_space_list:
                    no_space_list.remove(name1)
        self.community_identifiers_list = no_space_list
        return True

    def get_community_identifiers(self):
        return self.community_identifiers_list

    def add_alias(self, alias):
        self.community_identifiers_list.append(alias)
