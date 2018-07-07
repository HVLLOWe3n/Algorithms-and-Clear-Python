from unittest import TestCase

from Fibonachi_Digits_Algorithm.fibonach_digits import simple_fibonachi

#
# Class for testing file:
# fibonachi_digits.py
# Author code: @RomanDemyanchuk (HVLLOWe3n)
#


class Test_Fibonachi_Digits(TestCase):
    def test_nums(self):
        result = simple_fibonachi(5)

        self.assertEqual(5, result)
        self.assertNotEqual(13, result)