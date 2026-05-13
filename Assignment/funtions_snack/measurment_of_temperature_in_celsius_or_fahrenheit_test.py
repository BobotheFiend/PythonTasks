import unittest

import measurment_of_temperature_in_celsius_or_fahrenheit

class Testmeasurment_of_temperature_in_celsius_or_fahrenheit(unittest.TestCase):

#    def test_that_the_funtion_returns_a_conversion_in_fahrenheit(self):
#        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(50.0, "C")
#        expected = 122.0;
#        self.assertEqual(actual,expected)
#
#    def test_that_the_funtion_returns_a_conversion_in_celsius(self):
#        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(122.0, "F")
#        expected = 50.0;
#        self.assertEqual(actual,expected)
#
#    def test_that_the_funtion_returns_a_conversion_in_celsius_if_no_degree_c_or_f_was_selected(self):
#        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(50.0," ")
#        expected = 122.0;
#        self.assertEqual(actual,expected)

    def test_that_the_funtion_returns_heat_alert_without_input_of_c_or_f(self):
        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(50.0," ")
        expected = "Heat Alert";
        self.assertEqual(actual,expected)

    def test_that_the_funtion_returns_cold_advisory_without_input_of_c_or_f(self):
        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(0.0," ")
        expected = "Cold Advisory";
        self.assertEqual(actual,expected)

    def test_that_the_funtion_returns_heat_alert_with_the_input_of_celsius(self):
        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(50.0,"c")
        expected = "Heat Alert";
        self.assertEqual(actual,expected)

    def test_that_the_funtion_returns_heat_alert_with_the_input_of_fahrenheit(self):
        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(280.0,"f")
        expected = "Heat Alert";
        self.assertEqual(actual,expected)

    def test_that_the_funtion_returns_cold_advisory_with_the_input_of_celsius(self):
        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(0.0,"c")
        expected = "Cold Advisory";
        self.assertEqual(actual,expected)

    def test_that_the_funtion_returns_cold_advisory_with_the_input_of_fahrenheit(self):
        actual = measurment_of_temperature_in_celsius_or_fahrenheit.temperature_alert(100.0,"f")
        expected = "Cold Advisory";
        self.assertEqual(actual,expected)
