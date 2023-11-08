# api.py

import requests

class CalendarificAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_countries(self):
        url = 'https://calendarific.com/api/v2/countries?api_key=' + self.api_key
        response = requests.get(url)

        data = response.json()  # Parse results into a Python dictionary
        return data