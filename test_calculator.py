import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-2, 4), 2)
        self.assertEqual(add(0.1, 0.3), 0.4)

    def test_subtraction(self):
        self.assertEqual(subtract(2, 1)
        1)
        self.assertEqual(subtract(0, 7) - 7)
        self.assertEqual(subtract(-3, -2) - 1)

    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 2), 8)
        self.assertEqual(multiply(2, 2), 4)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(8, 4), 2)
        self.assertEqual(divide(9, 3), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(9, 0)

    def test_logaritm(self):
        self.assertEqual(logarithm(100, 10), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(5, 625), 4.0)

    def test_log_invalid_base(self):
        with self.asserRaises(ValueError):
            logarithm(1, 25)

    def test_log_invalud_argument(self):
        with self.asserRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError)
            square_root(-3)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
