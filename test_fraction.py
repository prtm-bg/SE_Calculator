import unittest
from fraction import FractionCalculator

class TestFractionCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = FractionCalculator()

    # addition
    def test_add(self):
        self.assertEqual(self.calc.calculate("4/5+3/5"), "7/5")

    # subtraction
    def test_subtract(self):
        self.assertEqual(self.calc.calculate("4/5-3/5"), "1/5")

    # multiplication
    def test_multiply(self):
        self.assertEqual(self.calc.calculate("2/3*3/4"), "1/2")

    # division
    def test_divide(self):
        self.assertEqual(self.calc.calculate("2/3/3/4"), "8/9")

    # simplification
    def test_simplify(self):
        self.assertEqual(self.calc.calculate("2/4+2/4"), "1/1")

    # invalid fraction
    def test_invalid_fraction(self):
        with self.assertRaises(ValueError):
            self.calc.calculate("3/0+1/2")

if __name__ == '__main__':
    unittest.main()