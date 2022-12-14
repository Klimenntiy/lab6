import unittest
from main import calcul

class calculTest(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calcul('1 + 2'), 3)

    def test_minus(self):
        self.assertEqual(calcul('1 - 2'), -1)

    def test_multi(self):
        self.assertEqual(calcul('3 * 2'), 6)

    def test_divide(self):
        self.assertEqual(calcul('6 / 2'), 3)
