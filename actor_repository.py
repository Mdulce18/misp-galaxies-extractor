# crear lista de actores, dar un nombre y buscarlo en la lista
import logging
import requests
# logging.basicConfig(level=logging.INFO)

from actor import Actor

# skip because ur


class Actor_Repository():
    def __init__(self, misp_json_link):
        self.misp_galaxy_json_link = misp_json_link
        # self.actors_aliases_list = []
        self.actors_list = []
        # self.description_list = []

    def parse_json(self):
        try:
            resp = requests.get(self.misp_galaxy_json_link)
            resp.raise_for_status()
        except requests.exceptions.MissingSchema:
            logging.error("Invalid URL Error")
            return None
        except requests.exceptions.InvalidSchema:
            logging.error("Invalid URL Error")
            return None
        except requests.exceptions.HTTPError:
            logging.error("Server Error: 500")
            return None

        return resp

    def create_actors_list(self):
        b = True  # b = True|None
        actor_counter = 0
        json = self.parse_json()

        while b is True:
            new_actor = Actor(actor_counter)
            b = new_actor.get_community_identifiers_json(json)
            if b is None:
                break
            else:
                raw_aliases = new_actor.get_raw_community_identifiers()
                new_actor.format_data(
                    new_actor.get_raw_community_identifiers())
                new_actor.get_community_identifiers()
                # self.actors_aliases_list.append(final_actor_list)
                self.actors_list.append(new_actor)
                actor_counter += 1

        return

    def create_aliases_list(self):
        aliases_list = []
        for actor in self.actors_list:
            aliases = actor.get_community_identifiers()
            aliases_list.append(aliases)
        return aliases_list

    def get_aliases_position(self, alias):
        actor_position = -1
        aliases_list = self.create_aliases_list()
        for actor in aliases_list:
            actor_position += 1
            if alias in actor:
                return actor_position
        return None

    def get_aliases(self, alias):
        position = self.get_aliases_position(alias)
        return self.actors_list[position].community_identifiers_list

    def get_description(self, alias):
        position = self.get_aliases_position(alias)
        return self.actors_list[position].description

    def get_actors_aliases_list(self):
        return self.actors_aliases_list

    def get_actors_list(self):
        return self.actors_list
