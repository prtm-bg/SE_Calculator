import unittest
from complex_add import add_complex


class TestComplexAdd(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add_complex((3, 2), (5, 3)), "8+5j")

    def test_add_negative(self):
        self.assertEqual(add_complex((-1, -2), (3, 4)), "2+2j")

    def test_add_zero(self):
        self.assertEqual(add_complex((0, 0), (0, 0)), "0+0j")


if __name__ == "__main__":
    unittest.main()