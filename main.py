# This file has to take the list of community identifiers and pass them to a csv
import logging

from config import misp_galaxy_json_link as link
from config import text_intro as intro
from actor_repository import Actor_Repository


def convert_list_to_string(org_list, seperator=''):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)


def search_for_alias(repository, alias_name):
    while alias_name != 'q':
        if alias_name is not None:
            alias_format = alias_name.lower().replace(' ', '_')
            aliases_position = repository.get_aliases_position(alias_format)
            # gather the position to search in repository of actor and descriptions
            if aliases_position is not None:
                aliases_list = repository.get_aliases(alias_format)
                aliases_formated = convert_list_to_string(aliases_list, ',')
                actor_description = repository.get_description(alias_format)
                actor_sources = repository.get_sources(alias_format)

                print(
                    f'Aliases:\n{aliases_formated}\nDescription:\n{actor_description}\nSources:')
                for source in actor_sources:
                    print(source)

            else:
                logging.error('Alias not found')

        alias_name = input('\nPlease enter an actor name or q to exit:\n')


def main():
    print(intro)
    new_repository = Actor_Repository(link)
    new_repository.create_actors_list()
    alias_name = None
    search_for_alias(new_repository, alias_name)
    print('Exiting...')


if __name__ == "__main__":
    main()
