import unittest
from calculator import add, subtract, multiply, divide, exponent, square_root, factorial, sin, cos, tan

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(1, 0), "Error! Division by zero.")

    def test_exponent(self):
        self.assertEqual(exponent(2), 4)
        self.assertEqual(exponent(-1), 1)
        self.assertEqual(exponent(0), 0)
        self.assertEqual(exponent(2.5), 6.25)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(6.25), 2.5)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(1.5)

    def test_trigonometric(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(45), 1)

if __name__ == '__main__':
    unittest.main()
