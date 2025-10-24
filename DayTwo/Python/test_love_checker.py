import unittest
from love_checker import two_in_love

class TestLoveChecker(unittest.TestCase):

	def test_love_even_odd(self):
		result = two_in_love(2, 3)
		self.assertTrue(result)

	def test_love_odd_even(self):
		result = two_in_love(5, 6)
		self.assertTrue(result)
	
	def test_love_both_odd(self):
		result = two_in_love(7, 9)
		self.assertFalse(result)

	def test_love_both_even(self):
		result = two_in_love(4, 8)
		self.assertFalse(result)
