# Exercise 2:
# 1. Provide a solution to get a weather forecast data of a particular city for next n days.
# 2. Consider leveraging the solution from Exercise 1 to get the days and use the same city that used for exercise 1.
# 3. Consider creating a class and methods to implement this solution
# 4. Write an automation test to test this function.

import requests
import json
from current_local_time import CalculateLocalTime
from datetime import datetime

class WeatherForecast(CalculateLocalTime):

    def __init__(self):
        self.forecast_report = {}

    def get_weather_report(self, location, days):
        # Endpoint for the weather API
        # http://api.weatherapi.com/v1/forecast.json?key=765856be42a9416dab9192612231803&q=Chennai&days=1&aqi=no&alerts=no

        next_no_days = days + 1
        url = "http://api.weatherapi.com/v1/forecast.json?q=" + location + "&days=" + str(next_no_days) + "&aqi=no&alerts=no"

        params = [
            {
                "q": "Chennai",
                "days": 10
            }
        ]
        headers = {"key": "765856be42a9416dab9192612231803",
                   "Content-Type": "application/json"}

        # Make a post request with the parameters.
        response = requests.post(url, json=params, headers=headers)

        # Print the content of the response
        wether_object = json.loads(response.content)

        for index, day in enumerate(wether_object["forecast"]["forecastday"]):
            if index > 0:
                self.forecast_report.update({
                    day["date"]: {
                        "Min-Temp-Celcius": day["day"]["mintemp_c"],
                        "Max-Temp_Celcius": day["day"]["maxtemp_c"]
                    }
                })

        return self.forecast_report


if __name__ == '__main__':
    place = input("Enter your place:")
    future_date = input("Enter future date in the format (Year-Month-Date) to calculate date difference")

    localtime = CalculateLocalTime()
    time = localtime.calculate_local_time(place)
    days = localtime.calculate_days(future_date)


    print("==========================================")
    print("Current local time for your location: ", time)
    print("Total number of left for the future days: ", days)
    print("==========================================")

    weather = WeatherForecast()
    report = weather.get_weather_report(place, days)
    print("Weather report for the next", str(days), "in the location", place, "is", report)
    print("==========================================")