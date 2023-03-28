# Write a function to return current local time and how many days left from current time.
# If input is (place = Chennai, future_date = '2022-12-25'), then function should returns its local time in Hours:Minutes:Seconds format and days as a integer.
# Also, write an automation test to test this function.

import datetime
import json

class CalculateLocalTime():

    def __init__(self):
        self.day_today = None
        self.future_day = None
        self.place = None
        self.total_days = None

    def calculate_local_time(self, place):
        # =============Approach by having a json file with all the UTC mapping timezones========================
        req_timezone = ""
        self.place = place
        timezone_data = open('timezone.json')
        data = json.load(timezone_data)
        for item in data:
            if self.place in item['text']:
                req_timezone = item['text']
                break
        utc_calc = req_timezone.split('(')[1].split(')')[0]
        offset_operator = utc_calc.split('UTC')[1][0]
        offset_hours = utc_calc.split('UTC')[1][1:].split(':')[0]
        offset_minutes = utc_calc.split('UTC')[1][1:].split(':')[1]
        timezone_data.close()

        if offset_operator == '+':
            time = (datetime.datetime.utcnow() + datetime.timedelta(hours=float(offset_hours),
                                                                    minutes=float(offset_minutes))) \
                .strftime('%H:%M:%S')
        else:
            time = (datetime.datetime.utcnow() - datetime.timedelta(hours=float(offset_hours),
                                                                    minutes=float(offset_minutes))) \
                .strftime('%H:%M:%S')

        return time


    def calculate_days(self, future_date):
        from datetime import datetime
        self.future_day = datetime.strptime(future_date, '%Y-%m-%d')
        date_today = datetime.now().today().date().strftime("%Y-%m-%d")
        self.day_today = datetime.strptime(date_today, '%Y-%m-%d')
        self.total_days = self.future_day - self.day_today
        return self.total_days.days