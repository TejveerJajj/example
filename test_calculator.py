import unittest
from calculator import add, subtract, multiply, divide, exponent

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

if __name__ == '__main__':
    unittest.main()
