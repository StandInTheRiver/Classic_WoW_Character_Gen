

class Singleton:

	__instance = None #class variable hidden, set to none

	@staticmethod
	def getInstance():
		if Singleton.__instance == None: #if its set to none - return the singleton class
			Singleton()
		else:
			return Singleton.__instance #if its not == none, return the instance of the singleton that was made before


	def __init__(self):
		if Singleton.__instance != None: #if instance is not = to None
			raise Exception("singleton already created") #display error 

		else:
			Singleton.__instance = self #if we dont have it created, set the instance to itself





s1 = Singleton()
print(s1)

#s2 = Singleton()
#print(s2)

s3 = s1.getInstance()
print(s3)

