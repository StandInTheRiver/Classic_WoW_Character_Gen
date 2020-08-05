
class Mediator:

	#defining the class to have something called colleagues, which begins as an empty list
	def __init__(self):
		self.colleagues = []


	#method, add colleague, takes a colleague and appends it to the colleagues list
	def add_colleague(self, colleague):
		self.colleagues.append(colleague)


	#when called, requires sender id, receipient and a msg
	def send_message(self, sender, reciever, msg): #for each existing colleague in the list
		for colleague in self.colleagues:
			if colleague.id == reciever: #if the colleagues id matches our target id
				colleague.recieve_message(sender, msg) #call that colleagues recieve method, giving it our sender and msg



class Colleague:


	#when creating this object - require id and mediator, call the add colleague funciton on creation
	def __init__(self, id, mediator):
		self.id = id
		self.mediator = mediator
		mediator.add_colleague(self)

	#when we want to send a message, we need the msg itself, who its going to, and were going to call mediator send message method and give it our id, target id and msg
	def send_message(self, id, msg):
		self.mediator.send_message(self.id,id,msg)

	#simply print the msg we got and the id's involved
	def recieve_message(self, id, msg):
		print ("ID " + str(self.id) + " recieved msg from id " + str(id) + \
				": " + msg)

class A(Colleague):

	pass

class B(Colleague):

	pass

class C(Colleague):

	pass

#Creates a mediator
mediator = Mediator()

#Creates class objects and assigns them an ID and a mediator
a1, a2, a3 = A(1,mediator), A(2,mediator), A(3,mediator)
b1, b2, b3 = B(4,mediator), B(5,mediator), B(6,mediator)
c1, c2, c3 = C(7,mediator), C(8,mediator), C(9,mediator)


#send the actual messages
c1.send_message(3, "first")
a3.send_message(7, "second")
b2.send_message(1, "third")