import unittest
import supermarket_inventory_manager_functions

class testing_supermarket_inventory_manager_functions(unittest.TestCase):

    def test_that_the_getTotal_functions_return_an_array_of_the_product_totals(self):
    
        product_lists = [[120, 95], [45, 60], [200, 175]]
        expected_result = supermarket_inventory_manager_functions.get_total(product_lists)
        actual_result = [215, 105, 375]
        self.assertEqual(actual_result, expected_result)

    def test_that_the_bestDay_return_the_best_days_for_each_product(self):
        
        product_lists = [[120, 95], [45, 60], [200, 175]]
        expected_result = supermarket_inventory_manager_functions.get_best_day(product_lists)
        actual_result = [1, 2, 1]
        self.assertEqual(actual_result, expected_result)

    def test_that_the_best_selling_product_function_returns_the_highest_unit_total(self):
        product_lists = [[120, 95], [45, 60], [200, 175]]
        expected_result = supermarket_inventory_manager_functions.the_best_selling_product_unit(product_lists)
        actual_result = 375
        self.assertEqual(actual_result, expected_result)

    def test_that_the_best_selling_product_function_returns_the_highest_product(self):
        product_lists = [[120, 95], [45, 60], [200, 175]]
        expected_result = supermarket_inventory_manager_functions.the_best_selling_product(product_lists)
        actual_result = 3
        self.assertEqual(actual_result, expected_result)


    def test_that_the_best_selling_product_function_returns_the_lowest_unit_total(self):
        product_lists = [[120, 95], [45, 60], [200, 175]]
        expected_result = supermarket_inventory_manager_functions.the_lowest_selling_product_unit(product_lists)
        actual_result = 105
        self.assertEqual(actual_result, expected_result)

    def test_that_the_best_selling_product_function_returns_the_lowest_product(self):
        product_lists = [[120, 95], [45, 60], [200, 175]]
        expected_result = supermarket_inventory_manager_functions.the_lowest_selling_product(product_lists)
        actual_result = 2
        self.assertEqual(actual_result, expected_result)

    def test_that_the_function_returns_total_number_of_units_sold(self):
        product_lists = [[120, 95], [45, 60], [200, 175]]
        expected_result = supermarket_inventory_manager_functions.overall_units_sold(product_lists)
        actual_result = 695
        self.assertEqual(actual_result, expected_result)
        

