# This file has to take the list of community identifiers and pass them to a csv
import logging

from config import misp_galaxy_json_link as link
from config import text_intro as intro
from actor_repository import Actor_Repository


def search_for_alias(repository, alias_name):
    while alias_name != 'q':
        if alias_name is not None:
            alias_format = alias_name.lower().replace(' ', '_')
            query = repository.get_aliases(alias_format)
            if query is not None:
                print(query)
            else:
                logging.error('Alias not found')

        alias_name = input('\nPlease enter an actor name or q to exit:\n')


def main():
    print(intro)
    new_repository = Actor_Repository(link)
    json_text = new_repository.parse_json()
    new_repository.create_actors_list(json_text)
    new_repository.get_actors_list()
    # print(full_repo)
    alias_name = None
    search_for_alias(new_repository, alias_name)
    print('Exiting...')


if __name__ == "__main__":
    main()
