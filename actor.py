# This class has to take the json file, then format the data and return the community identifiers.

import logging
import json
# logging.basicConfig(level=logging.INFO)

class Actor():  # Actor
    def __init__(self, actor_number):
        self.community_identifiers_list = []
        self.actor_number = actor_number
        self.community_identifiers_raw = []

    def get_community_identifiers_json(self, jsontext):
        # parse json from raw github
        try:
            data = json.loads(jsontext.text)
            try:
                # parse main actor name
                actor_name = data['values'][self.actor_number]['value']
            except IndexError:
                logging.info("Actor Index Error")
                return None
        except AttributeError:
            logging.error("JSON Parse Error")
            return None

        try:
            # parse community identifiers
            community_identifiers_raw = data['values'][self.actor_number]['meta']['synonyms']
            community_identifiers_raw.append(actor_name)
        except KeyError:
            logging.info(f"Actor {actor_name} without Aliases")
            community_identifiers_raw = [actor_name]

        self.community_identifiers_raw = community_identifiers_raw
        return True

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

    def get_raw_community_identifiers(self):
        return self.community_identifiers_raw

    def add_alias(self, alias):
        self.community_identifiers_list.append(alias)
