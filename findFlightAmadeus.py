from amadeus import Flights
import json

apiKey = "ahylFqLEHHhLjtNh43BgIVwMHMMkWgmC"
origin = "NYC"
departureDate = "2017-09-23"
duration = 1
maxPrice = 400

priceDestinations = "https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search"
topDestinations = "https://api.sandbox.amadeus.com/v1.2/travel-intelligence/top-destinations"

flights = Flights(apiKey)
resp = flights.inspiration_search(origin = origin, departure_date = departureDate, duration = duration, max_price = maxPrice)
print json.dumps(resp)
