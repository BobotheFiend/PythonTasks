import unittest

import function_check_for_palindriome_and_prime_number

class Test_function_check_for_palindriome_and_prime_number(unittest.TestCase):

    def test_the_function_collects_arguments(self):
        actual = function_check_for_palindriome_and_prime_number.palindrome_and_prime_checker(9)
        expected = False
        self.assertEqual(actual,expected)

    def test_the_function_collects_a_number_thats_not_prime_nor_palindrome_return_false(self):
        actual = function_check_for_palindriome_and_prime_number.palindrome_and_prime_checker(32432)
        expected = False
        self.assertEqual(actual,expected)


    def test_the_function_collects_a_number_thats_is_prime_but_not_palindrome_return_false(self):
        actual = function_check_for_palindriome_and_prime_number.palindrome_and_prime_checker(5059)
        expected = False
        self.assertEqual(actual,expected)

    def test_the_function_collects_a_number_thats_not_prime_but_a_palindrome_return_false(self):
        actual = function_check_for_palindriome_and_prime_number.palindrome_and_prime_checker(12321)
        expected = False
        self.assertEqual(actual,expected)

    def test_the_function_collects_a_number_thats_a_prime_and_palindrome_return_True(self):
        actual = function_check_for_palindriome_and_prime_number.palindrome_and_prime_checker(181)
        expected = True
        self.assertEqual(actual,expected)

    def test_the_function_collects_one_and_thats_not_prime_nor_palindrome_return_False(self):
        actual = function_check_for_palindriome_and_prime_number.palindrome_and_prime_checker(1)
        expected = False
        self.assertEqual(actual,expected)
