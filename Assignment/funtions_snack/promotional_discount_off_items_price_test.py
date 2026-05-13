import unittest

import promotional_discount_off_items_price

class Test_promotional_discount_off_items_price(unittest.TestCase):

    def test_the_function_collects_three_arguments(self):
        actual = promotional_discount_off_items_price.promotional_code("POLO",456.44,"Half")
        expected = "Invalid Promotional code..\nAll promo CODE must be in upperCase.\nCheck if ALL characters are in upperCase i.e(SAVE10 or HALFOFF)...\nNo discount! you're to pay 456.44"
        self.assertEqual(actual,expected)

    def test_the_function_collects_accepts_the_SAVE10_promo(self):
        actual = promotional_discount_off_items_price.promotional_code("PEN",500,"SAVE10")
        expected = 450
        self.assertEqual(actual,expected)


    def test_the_function_collects_accepts_the_HALFOFF_promo(self):
        actual = promotional_discount_off_items_price.promotional_code("BAG",15000,"HALFOFF")
        expected = 7500
        self.assertEqual(actual,expected)


    def test_the_function_doesnt_collect_a_promo_that_is_not_HALFOFF_or_SAVE10(self):
        actual = promotional_discount_off_items_price.promotional_code("SUIT",196000,"SAVEHALF")
        expected = "Invalid Promotional code..\nAll promo CODE must be in upperCase.\nCheck if ALL characters are in upperCase i.e(SAVE10 or HALFOFF)...\nNo discount! you're to pay 196000"
        self.assertEqual(actual,expected)


    def test_the_function_collects_accepts_the_SAVE10_promo_as_only_upperCase(self):
        actual = promotional_discount_off_items_price.promotional_code("TV",596000,"save10")
        expected = "Invalid Promotional code..\nAll promo CODE must be in upperCase.\nCheck if ALL characters are in upperCase i.e(SAVE10 or HALFOFF)...\nNo discount! you're to pay 596000"
        self.assertEqual(actual,expected)

    def test_the_function_collects_accepts_the_HALFOFF_promo_as_only_upperCase(self):
        actual = promotional_discount_off_items_price.promotional_code("A/C",478000,"halfoff")
        expected = "Invalid Promotional code..\nAll promo CODE must be in upperCase.\nCheck if ALL characters are in upperCase i.e(SAVE10 or HALFOFF)...\nNo discount! you're to pay 478000"
        self.assertEqual(actual,expected)

