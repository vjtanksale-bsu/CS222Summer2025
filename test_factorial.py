# test_math_ops.py
import unittest
from factorial import Factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(Factorial(0), 1)
        self.assertEqual(Factorial(5), 120)
        self.assertEqual(Factorial(1), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            Factorial(-1)

if __name__ == "__main__":
    unittest.main()
