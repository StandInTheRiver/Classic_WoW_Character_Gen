from abc import ABC, abstractmethod
#import ABC from abc, call it abstractmethod (a decorator)
import random

#abstract classes are classes that can have subtypes, but can never be created themselves


#network connection example

#ABC = abstract base class
#this class is defined to be an abstract base class
#its inheriting from abc, the module

#any children must have all the abstractmethods defined in the child to work
#you cannot define a networkconnection - it is abstract
#abstract classes lay out the framework for a real class, but do nothing themselves

class NetworkConnection(ABC):


	#all the things we want a generic networkconnection to do

	@abstractmethod
	def connect(self):
		pass #pass is python line that just says "were not gonna define it" similar to but a void in here

	@abstractmethod
	def send(self):
		pass

	@abstractmethod
	def disconnect(self):
		pass
###

class ConnectionA(NetworkConnection):

	def connect(self):
		print ("connection A established")

	def disconnect(self):
		print ("connection A disconnected")

	def send(self):
		print ("sending data with connection A....")
###	

class ConnectionB(NetworkConnection):

	def connect(self):
		print ("connection B established")

	def disconnect(self):
		print ("connection B disconnected")

	def send(self):
		print ("sending data with connection B....")
###	




#client code#
connectA = ConnectionA();
connectA.connect();
connectA.send();
connectA.disconnect();
#client code#


#do this 10 times...
connection_list = [];
for i in range(10):
	connection = ConnectionA() if random.randint(0,1) == 0 else ConnectionB() #make a random number betewen 0 and 1, if its 0 make connectionA object, if 1, make connecationB
	connection_list.append(connection); #append the connection we made to the array

#for each item in the  list, iterated by i, perform these methods
for i in range(10):
	connection_list[i].connect()
	connection_list[i].send()
	connection_list[i].disconnect()

#point is - we can call these methods we d efined in the parent class without any regard for what the actual methods do in the child classes