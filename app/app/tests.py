from django.test import TestCase

from app.calc import add, substract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that values are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        self.assertEqual(substract(5,6),1)
