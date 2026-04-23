import unittest
import largestnumberfunction

class Testlargestfunction(unittest.TestCase):
    def test_that_average_function_exists(self):
        largestnumberfunction.largest(55,4,99)
    def tesrt_that_largest_function_returns_correct_result(self):
        actual = largestnumberfunction.largest(55,4,99)
        expected = 99
        self.assertEqual(actual, expected)
