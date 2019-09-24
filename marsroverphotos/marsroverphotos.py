"""Main file for Mars rover photos app."""
import os
import json
from datetime import datetime

def load_config():
    """Load the project's configuration file."""
    try:
        app_dir = os.path.dirname(os.path.abspath(__file__))
        config_file = 'config.json'
        config_path = os.path.join(app_dir, config_file)
        with open(config_path) as infile:
            return json.load(infile)
    except (FileNotFoundError, IOError) as error:
        print('Unable to load config.  Exiting... {}'.format(error))
        raise

def load_dates_list(config):
    """Load the dates from a file to use for the Mars rover photos."""
    try:
        app_dir = os.path.dirname(os.path.abspath(__file__))
        dates_path = os.path.join(app_dir, config['resources_dir'], config['dates_file'])
        with open(dates_path) as infile:
            return infile.read().splitlines()
    except (FileNotFoundError, IOError) as error:
        print('Unable to load dates.  Exiting... {}'.format(error))
        raise

def get_strptime(supported_date_formats, date):
    """Converting a date string into a datetime.strptime object.
       This is also used to validate that the date is in a supported format."""
    exception_error = 'unsupported date format'
    for supported_date_format in supported_date_formats:
        try:
            return datetime.strptime(date, supported_date_format)
        except ValueError as error:
            if 'does not match format' not in str(error):
                exception_error = str(error)
    raise ValueError(exception_error)

class Marsroverphotos:
    """Class file for Mars rover photos app."""

    def __init__(self):
        """Init method for class."""
        self.config = load_config()
        self.dates_list = load_dates_list(self.config)
        self.dates = {}
        for date in self.dates_list:
            try:
                self.dates[date] = get_strptime(self.config['supported_date_formats'], date)
            except ValueError as error:
                print('Skipping {}... {}'.format(date, error))

    def run(self):
        """Main execution for running the Mars rover photos module/app"""


        print(self.dates)

if __name__ == "__main__":
    APP = Marsroverphotos()
    APP.run()
