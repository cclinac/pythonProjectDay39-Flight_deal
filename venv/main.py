# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

sheety_endpoint = "https://api.sheety.co/809b428ced075ed79fa674d0eb29cd8b/flightdeals/prices"
s_headers = {"Authorization": "Basic Y2hpbGk4OTU6YTE5ODgxMTI4"}
data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()
for _ in sheet_data:
    if _["iataCode"] == "":
        _["iataCode"] = flight_search.get_destination_code(_["city"])
print(f"sheet_data:\n {sheet_data}")
data_manager.get_destination_data = sheet_data
data_manager.update_destination_data()




