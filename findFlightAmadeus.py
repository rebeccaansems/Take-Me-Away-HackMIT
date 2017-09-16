import requests
import json
from Queue import Queue

apiKey = "ahylFqLEHHhLjtNh43BgIVwMHMMkWgmC"
origin = "BNA"
departureDate = "2017-09-23"
duration = 1
maxPrice = 250
period = "2016-09" # looking at most popular flights 1 year prior

priceDestinations = "https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search"
topDestinations = "https://api.sandbox.amadeus.com/v1.2/travel-intelligence/top-destinations"

def getDestinationList():
    payloadPrice = {"apikey": apiKey, "origin": origin, "departure_date": departureDate, "duration": duration, "max_price": maxPrice}
    destinationList = requests.get(priceDestinations, params=payloadPrice)
    destinationList = destinationList.json()

    destinations = dict()
    for each in destinationList['results']: # WONT WORK IF THERE'S NOTHING IN PRICE RANGE
        destinations[each['destination']] = each['price'] # we should check if price is maybe .5 of maxPrice
        # don't want to spend all the money at once

    return destinations

def getTopDestinations():
    payloadTopDestinations = {"apikey": apiKey, 'period': period, 'origin': origin}
    topDestinationList = requests.get(topDestinations, params=payloadTopDestinations)
    topDestinationList = topDestinationList.json()
    return topDestinationList

def getRelevantDestinations(destinationList, topDestinationList):
    relevantDestinations = Queue()
    for each in topDestinationList['results']:
        print each
        if each['destination'] in destinations: # it's included in possible price
            print each['destination'] + " price: " + destinations[each['destination']]
            relevantDestinations.put([each['destination'], destinations[each['destination']]])

    return relevantDestinations


destinations = getDestinationList()
topDestinationList = getTopDestinations()
relevantDestionations = getRelevantDestinations(destinations, topDestinationList)
