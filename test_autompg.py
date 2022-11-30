#import autompg
from autompg import AutoMPG
import unittest
from unittest.mock import patch, mock_open
from autompg import AutoMPGData 


class TestAutoMPG(unittest.TestCase):

    def test_str(self):
        # Create an AutoMPG object.
        # See if the __str__ function produces the expected output
        a = AutoMPG("Honda", "Ridgeline", "2022", "20")
        self.assertEqual(a.__str__(), 'Make: Honda  Model: Ridgeline  Year: 2022  MPG: 20.0')

    def test_eq(self):
        a = AutoMPG("Honda", "Ridgeline", "2022", "20")
        b = AutoMPG("Honda", "Ridgeline", "2022", "20")
        c = AutoMPG("Honda", "Passport", "2021", "25")
        self.assertTrue(a.__eq__(b))
        self.assertFalse(a.__eq__(c))

    def test_lt(self):

        a = AutoMPG("Honda", "Ridgeline", "2022", "20")
        b = AutoMPG("Honda", "Ridgeline", "2022", "20")
        c = AutoMPG("Honda", "Passport", "2021", "25")
        d = AutoMPG("Audi", "Sport Quattro S1", "1986", "10")
        e = AutoMPG("Ford", "Raptor", "2021", "15")
        self.assertTrue(d.__lt__(b))
        self.assertTrue(c.__lt__(b))
        self.assertTrue(c.__lt__(a))
        self.assertTrue(e.__lt__(a))
        self.assertTrue(e.__lt__(c))

    def test_load_data(self):
        a = "filename"
        

if __name__ == "__main__":
    unittest.main()