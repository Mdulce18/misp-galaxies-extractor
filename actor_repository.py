# crear lista de actores, dar un nombre y buscarlo en la lista
import logging
import requests
# logging.basicConfig(level=logging.INFO)

from actor import Actor

# skip because ur


class Actor_Repository():
    def __init__(self, misp_json_link):
        self.misp_galaxy_json_link = misp_json_link
        self.actors_list = []

    def parse_json(self):
        try:
            resp = requests.get(self.misp_galaxy_json_link)
            resp.raise_for_status()
        except requests.exceptions.MissingSchema:
            logging.error("Invalid URL Error")
            return None
        except requests.exceptions.HTTPError:
            logging.error("Server Error: 500")
            return None

        return resp

    def create_actors_list(self, json_text):
        b = True  # b = True|None
        actor_counter = 0
        json = json_text

        while b is True:
            new_actor = Actor(actor_counter)
            b = new_actor.get_community_identifiers_json(json)
            if b is None:
                break
            else:
                raw_aliases = new_actor.get_raw_community_identifiers()
                new_actor.format_data(
                    new_actor.get_raw_community_identifiers())
                final_actor_list = new_actor.get_community_identifiers()
                self.actors_list.append(final_actor_list)
                actor_counter += 1

        return True

    def get_aliases(self, alias):
        for actor in self.actors_list:
            # print(actor)
            if alias in actor:
                return actor

    def get_actors_list(self):
        return self.actors_list
