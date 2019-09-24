import os
import sys
import unittest
from datetime import datetime
from marsroverapp.marsroverphotos.marsroverphotos import Marsroverphotos
import urllib

class TestMarsroverphotos(unittest.TestCase):
    def setUp(self):
        self.config = {"resources_dir": "resources",
                  "dates_file": "dates.txt",
                  "supported_date_formats": ["%m/%d/%y", "%B %d, %Y", "%b-%d-%Y", "%m/%d/%Y"],
                  "downloads_dir": "downloads",
                  "api_key": "xExiSNivrhKvu1TMcWoxjninrDt7bqFhnWWVVfx9",
                  "mars_photos_api_string": "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={}-{}-{}&api_key={}"}

    def test_make_api_call_1(self):
        date = '2017-02-27'
        strp = datetime.strptime('02/27/2017', '%m/%d/%Y')
        photo = Marsroverphotos(self.config, strp)
        resp = photo.make_api_call()
        self.assertEqual(resp['photos'][0]['earth_date'], date)

    def test_make_api_call_2(self):
        strp = datetime.strptime('01/01/2017', '%d/%m/%Y')
        photo = Marsroverphotos(self.config, strp)
        photo.url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2017-2-31&api_key=xExiSNivrhKvu1TMcWoxjninrDt7bqFhnWWVVfx9'
        self.assertRaises(urllib.error.HTTPError, lambda: photo.make_api_call())

    def test_make_api_call_3(self):
        strp = datetime.strptime('01/01/2017', '%d/%m/%Y')
        photo = Marsroverphotos(self.config, strp)
        photo.url = 'https://api.nasa.gox/mars-photos/api/v9/rovers/curiosity/photo?earth_date=2017-2-31'
        self.assertRaises(urllib.error.URLError, lambda: photo.make_api_call())

    def test_get_img_src_1(self):
        strp = datetime.strptime('01/01/2017', '%d/%m/%Y')
        photo = Marsroverphotos(self.config, strp)
        img_src = 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01566/opgs/edr/fcam/FRB_536528163EDR_F0593016FHAZ00337M_.JPG'
        photo.get_img_src()
        self.assertEqual(photo.img_src, img_src)

    def test_get_img_src_2(self):
        strp = datetime.strptime('01/01/2099', '%d/%m/%Y')
        photo = Marsroverphotos(self.config, strp)
        img_src = ''
        photo.get_img_src()
        self.assertEqual(photo.img_src, img_src)

if __name__ == '__main__':
    unittest.main()
