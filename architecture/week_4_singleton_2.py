
class Singleton:

	__instance = None


	def __new__(cls): #new is used to create the object itself, init is for setting variables, new happens before Init

		if (cls.__instance is None):
			cls.__instance = super(Singleton,cls).__new__(cls) #all classes are a subtype of Object, this line calls superobject (object)s, New method to create it


		return cls.__instance



a = Singleton()

b = Singleton()
print(a)
print(b)