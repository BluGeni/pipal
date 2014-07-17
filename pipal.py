#!/usr/bin/env python3

import weather
import tod
import lights
#import face
import speech
#from RPi import GPIO
import config
#import curses

print("PiPal by Aaron Lehrian\n\n")

cfg = config.getConfig("pipal.cfg")

#SENSOR_PORT = int(cfg["SENSOR_PORT"])
NAME = cfg["NAME"]

def greetText(time_of_day, weather_conditions):
	return "Good " + time_of_day + " " + NAME + ". The current weather conditions are " + weather_conditions + ". " + tod.getComment()
	
def printLED():
	print("LED color: " + lights.getCurrentColor() + "\n\n")
	
	
def mainLoop():
#	GPIO.setmode(GPIO.BOARD)
#	GPIO.setup(SENSOR_PORT, GPIO.IN)

	lights.setRandom()
	printLED()

	try:
		while True:
			if input(''):
				if tod.checkTimer():
					time_of_day = tod.getTOD()
					weather_conditions = weather.getWeather()
					greet_text = greetText(time_of_day, weather_conditions["current_observation"]["weather"])
					print(greet_text + "\n")
					speech.playText(greet_text)
					lights.fade(weather.getColor(weather_conditions))
					printLED()
				tod.setTimer(10)
	except KeyboardInterrupt:
		pass
mainLoop()