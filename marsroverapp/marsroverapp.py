"""Main file for Mars rover photos app."""
import os
import json
from datetime import datetime
from marsroverapp.marsroverphotos import marsroverphotos

class Marsroverapp:
    """Class file for Mars rover photos app."""

    def __init__(self):
        """Init method for class."""
        self.app_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(self.app_dir, 'config.json')
        try:
            with open(config_path) as infile:
                self.config = json.load(infile)
                self.config['app_dir'] = self.app_dir
        except (FileNotFoundError, IOError) as error:
            print('Unable to load config: {}.  Exiting... {}'.format(config_path, error))
            raise

        self.dates_list = self.load_dates_list()
        self.dates = {}
        for date in self.dates_list:
            try:
                self.dates[date] = self.get_strptime(date)
            except ValueError as error:
                print('Skipping {}... {}'.format(date, error))

    def load_dates_list(self):
        """Load the dates from a file to use for the Mars rover photos."""
        try:
            dates_path = os.path.join(self.config['app_dir'],
                                      self.config['resources_dir'],
                                      self.config['dates_file'])
            with open(dates_path) as infile:
                return infile.read().splitlines()
        except (FileNotFoundError, IOError) as error:
            print('Unable to load dates from file: {}.  Exiting... {}'.format(dates_path, error))
            raise

    def get_strptime(self, date):
        """Converting a date string into a datetime.strptime object.
           This is also used to validate that the date is in a supported format."""
        exception_error = 'unsupported date format'
        for supported_date_format in self.config['supported_date_formats']:
            try:
                return datetime.strptime(date, supported_date_format)
            except ValueError as error:
                if 'does not match format' not in str(error):
                    exception_error = str(error)
        raise ValueError(exception_error)

    def run(self):
        """Main execution for running the Mars rover photos module/app"""

        for strp in self.dates.values():
            photos = marsroverphotos.Marsroverphotos(self.config, strp)
            photos.get_details()
            photos.download_image()
            photos.display_in_browser()
