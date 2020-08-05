import configparser
import redis
from newsapi import NewsApiClient
#singleton
class App():

	#hidden class variable
	__instance = None

	#from the tutorial, imports and connects to Redis DB
	def setup(self):
		config = configparser.ConfigParser()
		config.read("config.cfg")

		print(config["Database"]["host"])

		dbconn = redis.Redis(
			host= config["Database"]["host"],
			port= config["Database"]["port"],
			password= config["Database"]["password"],
			decode_responses= True)

		print(dbconn)
			
		newsapi = NewsApiClient(api_key='e0da1195f92c4ec7b5b29a03bc90e96a')


	#called before init, creates the object that init populates
	def __new__(cls):

		if(cls.__instance is None):
			cls.__instance = super(App, cls).__new__(cls) #all objcets have object as parent calss, calling super method -> calls python new method for object
			cls.__instance.setup()

		return cls.__instance



a = App()
b = App()

#both a and b are the same object, because this is a singleton
print(a)
print(b)



