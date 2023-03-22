import requests
import datetime as dt

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "NbDLIw9vsqQXTwcsgLSU12oGEl_KMG2P"
DEPARTURE_CITY = "LON"

class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        r = requests.get(url=location_endpoint, headers=headers, params=query)
        data = r.json()['locations'][0]['code']
        return data

    def search_flight(self, city_name):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        now = dt.datetime.now()
        query = {"fly_from": DEPARTURE_CITY,
                 "fly_to": city_name,
                 "dateFrom": "22/03/2023",
                 "dateTo": "22/04/2023",
                 }
        r = requests.get(url=search_endpoint, headers=headers, params=query)
        data = r.json()["data"][0]['price']
        print(data)
        return

flight_search = FlightSearch()
flight_search.search_flight("TPE")