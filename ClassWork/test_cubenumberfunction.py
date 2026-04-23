import unittest
import cubenumberfunction

class Testcubefunction(unittest.TestCase):
    def test_that_cube_function_exists(self):
        cubenumberfunction.cube(3)
    def test_that_cube_function_returns_correct_result(self):
        actual = cubenumberfunction.cube(3)
        expected = 27
        actual = cubenumberfunction.cube(5)
        expected = 125
        self.assertEqual(actual, expected)

    def test_that_cube_function_returns_invalid_data_type_with_wrong_input(self):
        actual = cubenumberfunction.cube("Nnmadi")
        expected = "Invalid input"
        self.assertEqual(actual, expected)
