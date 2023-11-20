import unittest
from unittest.mock import patch

import requests

from practice import divide_two_numbers


def mocked_get(*args, **kwargs):
    return "You already know Python!"


class TestDivideTwoNumbers(unittest.TestCase):
    def test_smoke(self):
        result = divide_two_numbers(4, 2)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_two_numbers(2, 0)

    @unittest.skip("Can't calculate")
    def test_skip_test(self):
        result = divide_two_numbers(6, 3)
        self.assertEqual(result, 3)

    @unittest.expectedFailure
    def test_expected_failure(self):
        result = divide_two_numbers(6, 2)
        self.assertEqual(result, 1)

    @patch("requests.get", side_effect=mocked_get)
    def test_mock(self, mock):
        response = requests.get("https://teachmeskills.by/kursy/qa-avtomatizirovannoe-testirovanie-na-python-online")

        self.assertEqual(response, "You already know Python!")
