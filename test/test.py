import unittest
from unittest.mock import patch 
from src.add import add, subtract

class TestFn(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        expected = 6
        actual = add(4, 2)
        self.assertEqual(expected, actual)
        
        expected = 4
        actual = add(0, 4)
        self.assertEqual(expected, actual)
        
    def test_subtract(self):
        expected = 2
        actual = subtract(4, 2)
        self.assertEqual(expected, actual)
        
        expected = -4
        actual = subtract(0, 4)
        self.assertEqual(expected, actual)
