import unittest
from complex_sub import subtract_complex


class TestComplexSub(unittest.TestCase):

    def test_sub_positive(self):
        self.assertEqual(subtract_complex((5, 3), (3, 2)), "2+1j")

    def test_sub_negative(self):
        self.assertEqual(subtract_complex((3, 2), (5, 3)), "-2-1j")

    def test_sub_zero(self):
        self.assertEqual(subtract_complex((0, 0), (0, 0)), "0+0j")


if __name__ == "__main__":
    unittest.main()