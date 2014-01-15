#!/usr/bin/python3

import weather
import tod
import lights
import face
import speech
from RPi import GPIO

print("PiPal by Aaron Lehrian\n\n")

SENSOR_PORT = 23
NAME = "Aaron"

def greetText(time_of_day, weather_conditions):
	return "Good " + time_of_day + " " + NAME + ". The current weather conditions are " + weather_conditions + ". " + tod.getComment()
	
def printLED():
	print("LED color: " + lights.getCurrentColor() + "\n\n")

def mainLoop():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(SENSOR_PORT, GPIO.IN)

	lights.setRandom()
	printLED()

	try:
		while True:
			if GPIO.input(SENSOR_PORT):
				if tod.checkTimer():
					time_of_day = tod.getTOD()
					weather_conditions = weather.getWeather()["current_observation"]["weather"]
					greet_text = greetText(time_of_day, weather_conditions)
					print(greet_text + "\n")
					speech.playText(greet_text)
					fade(weather.getColor(weather_conditions))
					printLED()
				tod.setTimer(10)
	except KeyboardInterrupt:
		GPIO.cleanup()

