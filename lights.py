#!/usr/bin/env python3

import time
import random
import os
import config

cfg = config.getConfig("pipal.cfg")

color = {
	"BLACK": [0, 0, 0],
	"WHITE": [255, 255, 255],
	"GRAY": [128, 128, 128],
	"SILVER": [192, 192, 192],
	"MAROON": [128, 0, 0],
	"RED": [255, 0, 0],
	"OLIVE": [128, 128, 0],
	"YELLOW": [255, 255, 0],
	"GREEN": [0, 128, 0],
	"LIME": [0, 255, 0],
	"TEAL": [0, 128, 128],
	"AQUA": [0, 255, 255],
	"NAVY": [0, 0, 128],
	"BLUE": [0, 0, 255],
	"PURPLE": [128, 0, 128],
	"FUCHSIA": [255, 0, 255],
	"PINK": [255, 192, 203],
	"HOTPINK": [255, 105, 180],
	"DEEPPINK": [255, 20, 147]
}

PORTS = [int(cfg['LED_PORT_1']), int(cfg["LED_PORT_2"]), int(cfg["LED_PORT_3"])]
DEFAULT_COLOR = str(cfg["DEFAULT_COLOR"])

def makeSet(color):
	if type(color) is str:
		return [int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)]
	elif type(color) is list:
		return color
		
current_color = makeSet(DEFAULT_COLOR)


def pwm(pin, angle):
	cmd = "echo " + str(pin) + "=" + str(angle/256) + " > /dev/pi-blaster"
	os.system(cmd)
	
def makeHex(color):
	if type(color) is list:
		return "#" + format(color[0],'x').zfill(2) + format(color[1],'x').zfill(2) + format(color[2],'x').zfill(2)
	elif type(color) is str:
		return color
		
def getCurrentHex():
	return makeHex(current_color)
			
def getCurrentColor():
	global color
	global current_color
	for key, value in color.items():
			if current_color == value:
				return key
	return getCurrentHex()

def setColor(hex):
	global current_color
	hex = makeSet(hex)
	pwm(PORTS[0], hex[0])
	pwm(PORTS[1], hex[1])
	pwm(PORTS[2], hex[2])
	current_color = hex
		
def randomHex():
	return "#" + format(random.randint(0,256**3-1),'x').zfill(6)

def randomColor():
	return [random.randint(0,256), random.randint(0,256), random.randint(0,256)]
	
def setRandom():
	setColor(randomColor())
	
def fade(color2, speed=5, steps=500, color1=-1):
	color2 = makeSet(color2)
	global current_color
	if color1 == -1:
		color1 = current_color
	else:
		color2 = makeSet(color2)
		
	sleep_time = speed/steps
	color_step = [(color2[0]-color1[0])/steps, (color2[1]-color1[1])/steps, (color2[2]-color1[2])/steps]
	
	for x in range(steps):
		color1 = [a + b for a, b in zip(color1, color_step)]
		setColor(color1)
		time.sleep(sleep_time)

def blink(colors=[color["BLACK"], color["WHITE"]],speed=.2,times=-1):
	if times == -1:
		try:
			while True:
				for color in colors:
					setColor(color)
					time.sleep(speed)
		except KeyboardInterrupt:
			return
	else:
		for x in range(times):
			for color in colors:
				setColor(color)
				time.sleep(speed)
