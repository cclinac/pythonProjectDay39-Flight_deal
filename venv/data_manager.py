import requests
import os

sheety_endpoint = "https://api.sheety.co/809b428ced075ed79fa674d0eb29cd8b/flightdeals/prices"
s_headers = {"Authorization": "Basic Y2hpbGk4OTU6YTE5ODgxMTI4"}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        s_response = requests.get(sheety_endpoint, headers=s_headers)
        data = s_response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_data(self):
        for _ in self.destination_data:
            new_data = {"price": {"iataCode": _['iataCode']}}
            p_response = requests.put(f"{sheety_endpoint}/{_['id']}", headers=s_headers, json=new_data)
            p_response.raise_for_status()

