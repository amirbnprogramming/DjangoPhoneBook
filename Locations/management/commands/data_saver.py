"""
    by using command line instuction you can fill the locations tables with data in csv files
    countries.csv
    states.csv
    cities.csv
"""
import csv
import os.path
from pathlib import Path
import logging
from django.core.management import BaseCommand

from Locations.models import Country, City, State

# Main Directory
data_path = Path(__file__).resolve().parents[3]

# CSV files
country_file = 'csvfiles/countries.csv'
states_file = 'csvfiles/states.csv'
cities_file = 'csvfiles/cities.csv'

# Configure the logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


class Command(BaseCommand):
    help = 'fill the tables with data in csv files'

    def add_arguments(self, parser):
        parser.add_argument('--start', action='store_true', help='Run filler')

    def handle(self, *args, **options):
        if options['start']:
            self.extract_save_data()

    def extract_save_data(self):
        # Delete history
        Country.delete_all_objects()
        State.delete_all_objects()
        City.delete_all_objects()
        logging.info('All pervious items deleted successfully.')

        # region countries  :
        with open(os.path.join(data_path, country_file), 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                # Extract data from each column
                id_ex = int(row[0].replace(" ", ""))
                name_ex = row[1].replace(" ", "")
                iso_name_ex = row[3].replace(" ", "")
                phone_code_ex = row[5].replace(" ", "")
                if phone_code_ex.startswith('+') or phone_code_ex.startswith('-'):
                    phone_code_ex = phone_code_ex[1:]

                if phone_code_ex.__contains__("and"):
                    phone_code_ex = phone_code_ex.split("and")[1]

                if phone_code_ex.__contains__("-"):
                    splited = phone_code_ex.split("-")
                    phone_code_ex = splited[0] + splited[1]

                extracted_country = Country(id=id_ex, name=name_ex, iso_name=iso_name_ex, phone_code=phone_code_ex)
                extracted_country.save()

                logging.info(f'Country : {extracted_country} extracted and saved in DB')
        self.stdout.write(self.style.SUCCESS('Country Items extracted successfully.'))
        # endregion

        # region states :
        with open(os.path.join(data_path, states_file), 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                # Extract data from each column
                id_ex = int(row[0].replace(" ", ""))
                name_ex = row[1].replace(" ", "")
                country_id_ex = int(row[2].replace(" ", ""))

                extracted_state = State(id=id_ex, name=name_ex, country_id=country_id_ex)
                extracted_state.save()

                logging.info(f'State : {extracted_state} extracted and saved in DB')
        self.stdout.write(self.style.SUCCESS('State Items extracted successfully.'))
        # endregion

        # region cities :
        with open(os.path.join(data_path, cities_file), 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                # Extract data from each column
                id_ex = int(row[0].replace(" ", ""))
                name_ex = row[1].replace(" ", "")
                state_id_ex = int(row[2].replace(" ", ""))

                extracted_city = City(id=id_ex, name=name_ex, state_id=state_id_ex)
                extracted_city.save()

                logging.info(f'City : {extracted_city} extracted and saved in DB')
        self.stdout.write(self.style.SUCCESS('Cities Items extracted successfully.'))
        # endregion
