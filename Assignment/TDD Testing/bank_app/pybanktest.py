import unittest
import pybank

class Testpybank(unittest.TestCase):
    #testing that the email function works
    def test_that_validate_email_function_exists(self):
        actual = pybank.validate_email('djth@45')
        expected = False;
        self.assertEqual(actual, expected)
        actual = pybank.validate_email('djth45u@yj')
        expected = True;
    def test_that_the_email_has_a_symbol_in_it(self):
        is_valid = pybank.validate_email("Tosin@avetium.org")
        self.assertTrue(is_valid) 
    def test_that_the_email_doesnt_have_a_symbol_and_throws_an_error(self):
        self.assertRaises(ValueError,pybank.validate_email,'tthateudgmailcome')


    #TestCalculateBalance    
    def test_that_calculate_balance_function_return_correct_balance(self):
        actual = pybank.calculate_balance([2500, 2000])
        expected = 4500
        self.assertEqual(actual, expected) 
    
        actual = pybank.calculate_balance([5000, 2000])
        expected = 7000
        self.assertEqual(actual, expected) 
        
        actual = pybank.calculate_balance([5000, -1000, 2000, -500])
        expected = 5500
        self.assertEqual(actual, expected)
        
    def test_that_calculate_balance_return_0_with_empty_transactions(self):
        actual = pybank.calculate_balance([])
        expected = 0
        self.assertEqual(actual, expected)




    #Testing that the password function works and checks all range
    def test_that_password_function_is_very_weak(self):
        actual = pybank.is_strong_password('thstays')
        expected = 'Your password is VERY WEAK'
        self.assertEqual(actual, expected)
    def test_that_is_strong_password_is_very_strong(self):
        actual = pybank.is_strong_password('djth45uyu66789uj44rrff')
        expected = 'Your password is VERY STRONG'
        self.assertEqual(actual, expected)       
    def test_that_is_is_strong_password_is_strong(self):
        actual = pybank.is_strong_password("password6")
        expected = 'Your password is STRONG'
        self.assertEqual(actual, expected)
       
        
    # TestApplyInterest  
    def test_that_apply_interest_function_return_correct_balance(self):
        actual = pybank.apply_interest(5000, 0.05, 10)
        expected = 8144.47
        self.assertEqual(actual, expected)
        
    def test_that_apply_interest_function_rate_can_not_be_negative(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, -0.05, 10)
        
    def test_that_apply_interest_function_years_can_not_be_less_than_one(self):
        with self.assertRaises(ValueError):
            pybank.apply_interest(5000, 0.05, 0.2)

    # TestGetTransactionSummary
    def test_that_get_transaction_summary_function_return_correct_summary(self):
        transactions = [["credit", 2000], ["debit", 500], ["credit", 1000]]
        actual = pybank.get_transaction_summary(transactions)
        expected = [["total_credits", 3000], ["total_debits", 500], ["net_balance", 2500], ["transaction_count", 3]]
        self.assertEqual(actual, expected)
