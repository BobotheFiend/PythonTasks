import unittest
import primenumber

class Testprimefunction(unittest.TestCase):
    def test_that_prime_function_exists(self):
        primenumber.prime_number(3)

    def test_that_prime_function_returns_false_result(self):
        actual = primenumber.prime_number(9)
        expected = False
        self.assertFalse(actual, expected)

    def test_that_prime_function_returns_True(self):
        actual = primenumber.prime_number(17)
        expected = True
        self.assertTrue(actual, expected)

    def test_that_prime_function_returns_True_with_wrong_input(self):
        actual = primenumber.prime_number(14)
        expected = False
        self.assertFalse(actual, expected)

    def test_that_the_prime_function_returns_false_with_large_inputs(self):
        actual = primenumber.prime_number(22344)
        expected = False
        self.assertFalse(actual, expected)
        actual = primenumber.prime_number(6636366)
        expected = False
        self.assertFalse(actual, expected)
        actual = primenumber.prime_number(7783344)
        expected = False
        self.assertFalse(actual, expected)

    def test_that_the_prime_function_returns_True_with_all_inputs(self):
        actual = primenumber.prime_number(19)
        expected = True
        self.assertTrue(actual, expected)
        actual = primenumber.prime_number(23)
        expected = True
        self.assertTrue(actual, expected)
        actual = primenumber.prime_number(41)
        expected = True
        self.assertTrue(actual, expected)
