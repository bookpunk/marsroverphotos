"""Main file for Mars rover photos object."""
import os
import json
from datetime import datetime
import urllib.request
import webbrowser

class Marsroverphotos:
    """Class file for Mars rover photos object."""

    def __init__(self, config, strp):
        """Init method for class."""
        self.config = config
        self.strp = strp
        self.date = datetime.strftime(strp, '%m/%d/%Y')
        self.file_name = ''
        self.file_path = ''
        self.img_src = ''
        self.api_results = {}

    def make_api_call(self, url):
        """Sends request to a URL and returns the JSON response."""
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read())
        except urllib.error.HTTPError as error:
            print('Skipping {}... HTTPError {} {}'.format(self.date, error.code, error.reason))
        except urllib.error.URLError as error:
            print('Skipping {}... URLError {} {}'.format(self.date, error.reason, url))

    def download_image(self):
        """Download photo specified by the img_src value of a Mars rover photo."""
        if self.img_src:
            self.file_name = self.img_src.split('/')[-1]
            self.file_path = os.path.join(self.config['app_dir'],
                                          self.config['downloads_dir'],
                                          self.file_name)
            try:
                urllib.request.urlretrieve(self.img_src, self.file_path)
            except urllib.error.HTTPError as error:
                print('Skipping {}... HTTPError {} {}'.format(self.date, error.code, error.reason))
            except urllib.error.URLError as error:
                print('Skipping {}... URLError {} {}'.format(self.date, error.reason, self.img_src))
        else:
            print('Skipping {}... no photos available'.format(self.date))

    def get_details(self):
        """Make a call to the API to get a response containing details about the
           photos from that day."""

        url = self.config['mars_photos_api_string'].format(self.strp.year,
                                                           self.strp.month,
                                                           self.strp.day,
                                                           self.config['api_key'])

        self.api_results = self.make_api_call(url)
        if self.api_results['photos']:
            self.img_src = self.api_results['photos'][0]['img_src']

    def display_in_browser(self):
        """Display the downloaded image in a browser."""
        if self.img_src:
            print('For {}, opening {}'.format(self.date, self.file_name))
            url = 'file://{}'.format(self.file_path)
            webbrowser.open(url, new=1, autoraise=True)