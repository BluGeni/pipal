#!/usr/bin/env python3

import configparser
import os

DEFAULT_CONFIG = """[DEFAULT]
NAME = Aaron
KEY = c75d167e83b5193c
LOCATION = pws:KFLJACKS18
DEFAULT_COLOR = #000000
UNKNOWN_WEATHER_COLOR = #008000
TEMP_PATH = 
SENSOR_PORT = 16
LED_PORT_1 = 4
LED_PORT_2 = 17
LED_PORT_3 = 22"""

def createConfig():
	dir = "."
	if not os.path.exists(dir):
		os.makedirs(dir)
	config_file = dir + "/pipal.cfg"
	f = open(config_file, 'w')
	f.write(DEFAULT_CONFIG)
	f.close()
	

def getConfig(file):
	try:
		with open(file):
			config = configparser.ConfigParser()
			config.read(file)
			return config["DEFAULT"]
	except IOError:
		createConfig()
		return getConfig(file)