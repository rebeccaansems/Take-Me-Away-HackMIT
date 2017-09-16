import requests
import json

apiKey = "ahylFqLEHHhLjtNh43BgIVwMHMMkWgmC"
origin = "NYC"
departureDate = "2017-09-23"
duration = 1
maxPrice = 400
period = "2016-09"

priceDestinations = "https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search"
topDestinations = "https://api.sandbox.amadeus.com/v1.2/travel-intelligence/top-destinations"

payloadPrice = {"apikey": apiKey, "origin": origin, "departure_date": departureDate, "duration": duration, "max_price": maxPrice}
destinationList = requests.get(priceDestinations, params=payloadPrice)
destinationList = destinationList.json()

payloadTopDestinations = {"apikey": apiKey, 'period': period, 'origin': origin}
topDestinationList = requests.get(topDestinations, params=payloadTopDestinations)
topDestinationList = topDestinationList.json()

for each in destinationList['results']:
    print each['destination']

from Queue import Queue
for each in topDestinationList['results']:
    if each['destination'] in
