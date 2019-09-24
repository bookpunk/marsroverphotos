import os
import sys
import unittest
from datetime import datetime
from marsroverapp.marsroverapp import Marsroverapp

class TestMarsroverapp(unittest.TestCase):
    def setUp(self):
        self.func = Marsroverapp()
        self.func.config = {"supported_date_formats": ["%m/%d/%y", "%B %d, %Y", "%b-%d-%Y", "%m/%d/%Y"]}
 
    def test_get_strptime_1(self):
        self.assertRaises(ValueError, lambda: self.func.get_strptime('April 31, 2018'))

    def test_get_strptime_2(self):
        self.assertRaises(ValueError, lambda: self.func.get_strptime('10*11*19'))

    def test_get_strptime_3(self):
        date = '02/27/17'
        expected_strp = datetime.strptime(date, '%m/%d/%y')
        strp = self.func.get_strptime(date)
        self.assertEqual(expected_strp, strp)

    def test_get_strptime_4(self):
        date = '02/28/2017'
        expected_strp = datetime.strptime(date, '%m/%d/%Y')
        strp = self.func.get_strptime(date)
        self.assertEqual(expected_strp, strp)
  
    def test_get_strptime_5(self):
        date = 'June 2, 2018'
        expected_strp = datetime.strptime(date, '%B %d, %Y')
        strp = self.func.get_strptime(date)
        self.assertEqual(expected_strp, strp)

    def test_get_strptime_6(self):
        date = 'October 31, 2099'
        expected_strp = datetime.strptime(date, '%B %d, %Y')
        strp = self.func.get_strptime(date)
        self.assertEqual(expected_strp, strp)

    def test_get_strptime_7(self):
        date = 'Jul-13-2016'
        expected_strp = datetime.strptime(date, '%b-%d-%Y')
        strp = self.func.get_strptime(date)
        self.assertEqual(expected_strp, strp)

if __name__ == '__main__':
    unittest.main()
