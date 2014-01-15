#!/usr/bin/python3

import urllib.request
from pydub import AudioSegment
import os

def parseText(text):
	text_list = []
	while len(text) > 100:
		text_list.append(text[0:100])
		text = text[100:]
		
	text_list.append(text)
	return text_list
	
def getMp3(text_list):
	file_list = []
	x = 0
	for line in text_list:
		file_list.append["line" + str(x) + ".mp3"]
		url = "http://translate.google.com/translate_tts?tl=en&q=" + line
		with urllib.request.urlopen(url) as response, open(file_list[x], 'wb') as out_file:
			data = response.read()
			out_file.write(data)
			response.close()
			out_file.close()
		x = x + 1
	return file_list

def combineMp3(file_list, out_file="speech.mp3"):
	mp3_list = []
	for file in file_list:
		mp3_list.append(AudioSegment.from_mp3(file))
	
	speech = reduce(lambda a, b: a + b, mp3_list)
	speech.export("speech.mp3", format="mp3")
	return speech
	
def playText(text):
	text_list = parseText(text)
	file_list = getMp3(text_list)
	combineMp3(file_list, "speech.mp3")

	os.system("mpg123 -q speech.mp3")
	
	for file in file_list:
		os.remove(file)
	
	os.remove("speech.mp3")