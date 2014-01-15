#!/usr/bin/python3

import urllib.request
import json
import lights
import config

cfg = config.getConfig("pipal.cfg")

UNKNOWN_WEATHER_COLOR = cfg["UNKNOWN_WEATHER_COLOR"]
KEY = cfg["KEY"]
LOCATION = cfg["LOCATION"]

COLOR = {
	"Rain": lights.color["BLUE"],
	"Fog": lights.color["GRAY"],
	"Thunderstorm": lights.color["PURPLE"],
	"Cloud": lights.color["WHITE"],
	"Clear": lights.color["YELLOW"],
	"Unknown": lights.randomColor(),
	"Smoke": lights.color["SILVER"],
	"Drizzle": lights.color["TEAL"],
	"Snow": lights.color["MAROON"],
	"Hail": lights.color["LIME"]
}

def searchDict(dict, lookup):
	for key, value in dict.items():
		if key in lookup:
			return value
	return UNKNOWN_WEATHER_COLOR

def getWeather(loc=LOCATION):
	url = "http://api.wunderground.com/api/" + KEY + "/geolookup/conditions/q/" + loc + ".json"
	with urllib.request.urlopen(url) as response:
		json_string = response.read().decode('utf-8')
		parsed_json = json.loads(json_string)
		response.close()
	return parsed_json
	
def getColor(weather):
	weather = weather["current_observation"]["weather"]
	return searchDict(COLOR, weather)