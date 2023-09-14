import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_discount_returns_price_as_zero_when_called_with_more_than_three_prices(self):
        prices = [10, 4, 20, 16]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_negative_prices_under_three_entries(self):
        prices = [10, -4, 20]
        expected_discount = -4
        self.assertEqual(expected_discount, discount(prices))

    # TODO more unit tests here. Each test should test one scenario


if __name__ == '__main__':
    unittest.main()