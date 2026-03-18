# test_complex.py
import unittest
from complex import (
    parse_complex_string, add_complex, subtract_complex, 
    multiply_complex, divide_complex, compute_magnitude, 
    compute_phase, evaluate_complex_expression
)

class TestComplexArithmetic(unittest.TestCase):

    # --- Parser Tests ---
    def test_parse_complex_string_valid(self):
        c1, op, c2 = parse_complex_string('(3 + 2j) * (5+ 3j)')
        self.assertEqual(c1, '3+2j')
        self.assertEqual(op, '*')
        self.assertEqual(c2, '5+3j')

    def test_parse_complex_string_invalid(self):
        # Boundary Condition: Missing brackets should raise a ValueError
        with self.assertRaises(ValueError):
            parse_complex_string('3+2j * 5+3j')

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

    def test_divide_complex_by_zero(self):
        # Test division by zero exception handling
        pass

    # --- Member 4 Tests ---
    def test_compute_magnitude(self):
        # Test magnitude calculations
        pass

    def test_compute_phase(self):
        # Test phase calculations (check against known angles)
        pass

    # --- Member 5 Tests (Integration) ---
    def test_evaluate_complex_expression(self):
        # Test the full pipeline from raw string to final output
        pass

if __name__ == "__main__":
    unittest.main()