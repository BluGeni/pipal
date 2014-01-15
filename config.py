import configparser

def getConfig(file):
	config = configparser.ConfigParser()
	config.read(file)
	return config["DEFAULT"]