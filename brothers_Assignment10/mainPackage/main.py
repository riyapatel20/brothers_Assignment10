# Name: Riya Patel and Emma Wilson 
# email: patel5ry@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/09/23
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that I can use Eclipse to extract information from an API. 
# Citations: https://calendarific.com/api-documentation
# Anything else that's relevant: N/A

# main.py

from apiPackage.api import CalendarificAPI

if __name__ == "__main__":
    api_key = 'dM2voClzuCOUJgzo9zOn0BG8CmxAPlvx'
    calendarific_api = CalendarificAPI(api_key)

    countries_data = calendarific_api.get_countries()  # Get a parsed dictionary from the API response

    if countries_data:
        countries = countries_data.get('response', {}).get('countries', [])  # Extract the list of countries

        if countries:
            for country in countries:
                country_name = country.get('country_name')  # Get the country names
                print(country_name)  # Print some very interesting information

