# test_complex.py
import unittest
from complex import (
    parse_complex_string, add_complex, subtract_complex, 
    multiply_complex, divide_complex, compute_magnitude, 
    compute_phase, evaluate_complex_expression
)
import math
class TestComplexArithmetic(unittest.TestCase):

    # --- Member 1 Tests ---
    def test_parse_complex_string_valid(self):
        # Test normal valid strings here
        pass

    def test_parse_complex_string_invalid(self):
        # Test malformed strings or missing brackets here
        pass

    # --- Member 2 Tests ---
    def test_add_complex(self):
        # Test normal addition and negative addition
        pass

    def test_subtract_complex(self):
        # Test normal subtraction
        pass

    # --- Member 3 Tests ---
    def test_multiply_complex(self):
        # Lab manual example test case 
        self.assertEqual(multiply_complex('1+2j', '3+4j'), '-5+10j')

    def test_divide_complex(self):
        # Test normal division
        pass

    def test_compute_magnitude(self):
    # Test magnitude calculations
        self.assertAlmostEqual(compute_magnitude('3+4j'), 5.0)
        self.assertAlmostEqual(compute_magnitude('1+0j'), 1.0)
        self.assertAlmostEqual(compute_magnitude('0+2j'), 2.0)


    def test_compute_phase(self):
        # Test phase calculations (check against known angles)
        self.assertAlmostEqual(compute_phase('1+0j'), 0.0)
        self.assertAlmostEqual(compute_phase('0+1j'), math.pi/2)
        self.assertAlmostEqual(compute_phase('-1+0j'), math.pi)

    def test_compute_phase(self):
        # Test phase calculations (check against known angles)
        pass

    # --- Member 5 Tests (Integration) ---
    def test_evaluate_complex_expression(self):
        # Test the full pipeline from raw string to final output
        pass

if __name__ == "__main__":
    unittest.main()