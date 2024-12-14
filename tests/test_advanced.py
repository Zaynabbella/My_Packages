"""
Tests for advanced mathematical operations.
"""

import unittest
from mathops.advanced import power, square_root

class TestAdvancedOperations(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(5, 2), 25)

    def test_square_root(self):
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)