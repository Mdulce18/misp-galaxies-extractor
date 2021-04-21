# This file has to take the list of community identifiers and pass them to a csv
from config import misp_galaxy_json_link as link

from actor_repository import Actor_Repository

new_repository = Actor_Repository(link)
json_text = new_repository.parse_json()
new_repository.create_actors_list(json_text)
full_repo = new_repository.get_actors_list()
print(full_repo)
list1 = new_repository.get_aliases('apt1')
print(list1)
