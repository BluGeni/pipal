#!/usr/bin/python3

from datetime import datetime
import time
import random

current_time = datetime.now()
timer_time = time.time()
timer_length = 0

MORNING_COMMENTS = [
	"Have a good day!",
	"Start your day off right!",
	"Don't forget to eat breakfast!"
]

AFTERNOON_COMMENTS = [
	"I hope your day has been going well.",
	"Keep on chugging today!"
]

EVENING_COMMENTS = [
	"Don't forget to eat dinner!",
	"Shouldn't you be practicing right now?",
	"I hope your day has been good."
]

NIGHT_COMMENTS = [
	"Don't stay up too late!",
	"Try not to late night snack.",
	"Stay away from the caffeine now!"
]

def updateTime():
	global current_time
	current_time = datetime.now()
	return current_time
	
def getTOD():
	hour = updateTime().hour
	if 5 <= hour <= 11:
		return "morning"
	elif 12 <= hour <= 17:
		return "afternoon"
	elif 18 <= hour <= 20:
		return "evening"
	else:
		return "night"

def getComment():
	hour = updateTime().hour
	if 5 <= hour <= 11:
		return MORNING_COMMENTS[random.randint(0, len(MORNING_COMMENTS)-1)]
	elif 12 <= hour <= 17:
		return EVENING_COMMENTS[random.randint(0, len(AFTERNOON_COMMENTS)-1)]
	elif 18 <= hour <= 20:
		return AFTERNOON_COMMENTS[random.randint(0, len(EVENING_COMMENTS)-1)]
	else:
		return NIGHT_COMMENTS[random.randint(0, len(NIGHT_COMMENTS)-1)]
		
def setTimer(minutes=5):
	global timer_time, timer_length
	timer_length = minutes * 60
	timer_time = time.time()
	
def checkTimer():
	global timer_time, timer_length
	if time.time()-timer_time >= timer_length:
		return True
	else:
		return False

#TODO: add calendar events