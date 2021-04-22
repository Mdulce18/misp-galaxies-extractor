import logging
import csv
from datetime import datetime

from config import misp_galaxy_json_link as link
from config import text_intro as intro
from actor_repository import Actor_Repository


def write_actors_in_csv(list_actors, file_name):

    with open(f'./csv_files/{file_name}', "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(list_actors)
     # logging.error(f'Error creating {file_name} file')


def main():
    now = datetime.now()
    date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
    file_name = f'comunity_dentifiers_{date_time}'

    new_repository = Actor_Repository(link)
    json_text = new_repository.parse_json()
    new_repository.create_actors_list(json_text)
    data = new_repository.get_actors_list()
    try:
        write_actors_in_csv(data, f'{file_name}.csv')
        print('CSV created. Exiting...')
    except:
        logging.error('CSV Creation Error')


if __name__ == "__main__":
    main()
