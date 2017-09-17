import requests
import json


def getCurrentLatLong():
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j = json.loads(r.text)
	return ', '.join([str(j['latitude']), str(j['longitude'])]);

def getCurrentCity():
	send_url = 'http://freegeoip.net/json'
	r = requests.get(send_url)
	j = json.loads(r.text)
	return j['city']