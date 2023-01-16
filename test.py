import unittest
from utils import check_type, add_fish_to_aquarium

import unittest



class TestTypeChecker(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.test_strings = "ADHDHDHDHDHDD"
        self.test_int = 12
        self.test_enum = [ "ABCDEFGHIJKLMNOPQRSTUVWXYZA", "ABCDEFGHIJKLMNOPQ", "ABCDEFGHIJKLMNOPQRSTUVW", "ABCDEFGHIJKLMNOPQRSTUVWXY", "ABCDEFGHIJK" ]
        self.test_array = {
        "id": "ABCDEFGHIJKLMNOP",
        "nickname": "ABCD",
        "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
        "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "countryCode": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "orientation": "ABCDEFGHIJKLMNOPQRSTU"
      }

    def test_string_type(self):
        actual = check_type(self.test_strings)
        expected = "string"
        self.assertEqual(actual, expected)

    def test_integer_type(self):
        actual = check_type(self.test_int)
        expected = "integer"
        self.assertEqual(actual, expected)

    def test_enum_type(self):
        actual = check_type(self.test_enum)
        expected = "enum"
        self.assertEqual(actual, expected)

    def test_array_type(self):
        actual = check_type(self.test_array)
        expected = "array"
        self.assertEqual(actual, expected)







