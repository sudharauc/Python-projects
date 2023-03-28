import unittest
from datetime import datetime
from datetime import timedelta
from current_local_time import CalculateLocalTime
from weather_forecast import WeatherForecast


class LocalTimeTest(unittest.TestCase):

    def test_localtime_positive_case(self):
        expected_date = datetime.now().strftime("%H:%M:%S")
        time_object = CalculateLocalTime()
        actual_date = time_object.calculate_local_time(place="Chennai")
        self.assertEqual(expected_date, actual_date, "The actual method calculated date incorrect for the time zone.")

    def test_localtime_negative_case(self):
        expected_date = "14:11:16"
        time_object = CalculateLocalTime()
        actual_date = time_object.calculate_local_time(place="Chennai")
        self.assertNotEqual(expected_date, actual_date, "The actual method calculated date incorrect for the time zone.")

    def test_date_difference(self):
        time_object = CalculateLocalTime()
        days = time_object.calculate_days(future_date="2023-3-26")
        self.assertEqual(7, days, "The actual method calculated date incorrect for the time zone.")

    def test_weather_positive_case(self):
        wether = WeatherForecast()

        actual_response = wether.get_weather_report("Chennai", 2)
        today_date = datetime.today().date()
        end_date = today_date + timedelta(days=2)
        self.assertTrue(str(today_date + timedelta(days=1)) in actual_response.keys(),
                        "The date is not found in the report")
        self.assertTrue(str(end_date) in actual_response.keys(), "The date is not found in the report")
        self.assertEqual(2, len(actual_response.keys()), "The expected number of records not found")
        for date_response in actual_response:
            self.assertIsNotNone(actual_response[date_response]['Min-Temp-Celcius'],
                                 "The min temperature not found in the response")
            self.assertIsNotNone(actual_response[date_response]['Max-Temp_Celcius'],
                                 "The max temperature not found in the response")



if __name__ == '__main__':
    unittest.main()
