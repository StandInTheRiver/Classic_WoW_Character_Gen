from abc import ABC, abstractmethod
import numpy
import redis
import os
from wowapi import WowApi
import random
import string

class Singleton:

	__instance = None #class variable hidden, set to none
	r = redis.Redis(
	host="redis-14585.c11.us-east-1-3.ec2.cloud.redislabs.com",
	port="14585",
	password="TMgOol2qM6wjkypZ1qrbaovjJcRXTpy2",
	decode_responses=True
	)
	w = WowApi('d8ce5f1aecbd4edb800cbd753ac529a6', 'eZtkVNmDUxqjHd8Pn0msignc3xvBh5v5')

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

	def cls(self):
		os.system('cls' if os.name=='nt' else 'clear')
class Api():
	def get_classes(self):
		get = data.w.get_playable_class_index('us', 'static-classic-us', locale='en_US')
		return get

	def get_races(self):
		get = data.w.get_playable_race_index('us', 'static-classic-us', locale='en_US')
		return get
class Redis():

	def get_questions(self):
		get = data.r.lrange("questions", 0, -1)
		return get

	def get_data(self, name):
		self.name =  name
		get = data.r.lrange(self.name, 0, -1)
		return get

	def add_to_db(self, key, result, table):
		self.key = key
		self.result = result
		self.table = table
		data.r.hset(self.table, str(self.key), str(self.result))

	def get_saved(self, key):
		self.key = key
		print("redis key to be sent" + str(self.key))
		return data.r.hget("Saved_Characters",str(self.key))
class Interface():

	def main(self):
		data.cls()
		print("select an option")
		print("Press 1 for new character")
		print("Press 2 for random character")
		print("Press 3 for load character")
		self.x = input("")
		if self.x == "1":
			Interface.new_character(self)
		if self.x == "2":
			Interface.random_character(self)
		if self.x == "3":
			Interface.load_character(self)
	def new_character(self):
		data.cls()
		print("new character menu")
		print("type 1 to start creating a new character")
		print("Type 9 to go back to main menu")
		self.x = input("")
		if self.x == "9":
			Interface.main(self)
			self.x = None
		if self.x == "1":
			Controller.new_character(self, "build")
	def random_character(self):
		data.cls()
		print("Random character menu")
		print("type 1 to create a random character")
		print("Type 9 to go back to main menu")
		self.x = input("")
		if self.x == "9":
			Interface.main(self)
			self.x = None
		if self.x == "1":
			Controller.new_character(self, "random")
			self.x = None
	def load_character(self):
		data.cls()
		print("Load character menu")
		print("type 1 to start loading your charcter")
		print("Type 9 to go back to main menu")
		self.x = input("")
		if self.x == "9":
			Interface.main(self)
			self.x = None
		if self.x == "1":
			data.cls()
			print("enter your character string")
			self.x = input("")
			print(self.x)
			save_query = Controller.load_character(self, self.x)
			self.result_page(save_query, self.x)
	def result_page(self, result, option):
		self.x = None
		self.result = result
		self.option = option
		data.cls()
		print("Your results are: " + str(self.result))
		print(self.option)
		print("Type 9 to go back to main menu")
		self.x = input("")
		if self.x == "9":
			Interface.main(self)
			self.x = None
	def ask_questions(self, question_array):
		self.question_array = question_array
		self.answer = Controller.create_array_with_size(self, self.question_array)
		data.cls()
		k = 0
		for i in self.question_array:
			print("Answer Each question with a value between 0 and 3")
			print("Type 9 to go back to main menu")
			print(" 0 = Strongly Disagree")
			print(" 1 = Disagree")
			print(" 2 = Agree")
			print(" 3 - Strongly Agree")
			print(" ")
			self.answer[k] = input(i + " : ")
			k = k + 1
			data.cls()
		k = 0
		for i in self.answer:
			if i == "0":
				self.answer[k] = "0.25"
				k = k + 1
			if i == "1":
				self.answer[k] = "0.5"
				k = k + 1
			if i == "2":
				self.answer[k] = "1.5"
				k = k + 1
			if i == "3":
				self.answer[k] = "2.0"
				k = k + 1
		return self.answer
class Controller():

	def create_array_with_size(self, array):
		self.array = array
		return numpy.empty(len(self.array), dtype=object)



	def new_character(self, type):
		self.type = type
		self.factory = Factory()
		if self.type == "build":
			x = Model.call_db_list(self, "questions")
			y = Interface.ask_questions(self, x)
			z = self.factory.create_character("fresh", y)
			z.test()
			z.calculate_final_result()
			answer = z.report()
			Model.call_db_add(self, z.key, answer)
			Interface.result_page(self, answer, z.key)
		if self.type == "random":
			z = self.factory.create_character("random", None)
			z.calc_random()
			answer = z.report()
			Model.call_db_add(self, z.key, answer)
			Interface.result_page(self, answer, z.key)			

	def load_character(self, key):
		self.key = key
		print(self.key)
		return Model.call_db_saved(self, self.key)
class Model():


	def call_wow_api(self, type):
		self.type = type

		if self.type == "Classes":
			return Api.get_classes(self)

		if self.type == "Races":
			return Api.get_races(self)
		
	def call_db_list(self, type):
		self.type = type
		if self.type == "questions":
			return Redis.get_questions(self)

	def call_db_single(self, name):
		self.name = name
		return Redis.get_data(self, self.name)

	def call_db_add(self, key, result):
		self.key = key
		self.result = result
		Redis.add_to_db(self, self.key, self.result, "Saved_Characters")

	def call_db_saved(self, key):
		self.key = key
		return Redis.get_saved(self, self.key)
class Factory():

	def create_character(self, type, question_result):
		self.type = type
		self.question_result = question_result
		if self.type == "fresh":
			x = []
			alliance_base = Model.call_db_single(self, "Alliance")
			horde_base = Model.call_db_single(self, "Horde")
			races_index = Model.call_wow_api(self, "Races")
			classes_index = Model.call_wow_api(self, "Classes")
			for i in races_index["races"]:
				race_name = i["name"]
				if race_name == "Night Elf":
					race_name = "Nightelf"
				x.append(Model.call_db_single(self, race_name))	
			for i in classes_index["classes"]:
				class_name = i["name"]
				x.append(Model.call_db_single(self, class_name))
			for i in x:
				print(i)
			#create new Character Class
			#call character initialize to give it all the values it needs
			x.append(alliance_base)
			x.append(horde_base)
			return Character(x, self.question_result)

		if self.type == "random":
			return Character(None, None)





	def create_array(self, name, size):
		self.name = name
		self.size = size
class Character():
	def __init__(self, base_values, question_result):
		self.base_values = base_values
		self.question_result = question_result
		self.absolute_final_result = None
		self.key = self.gen_key()
		print(self.question_result)
		print("go")
	def test(self):
		print("test sucessed")


	def calc_random(self):
			valid_races = numpy.empty(8, dtype=numpy.object)
			valid_races[0] = "human"
			valid_races[1] = "orc"
			valid_races[2] = "dwarf"
			valid_races[3] = "nightelf"
			valid_races[4] = "undead"
			valid_races[5] = "tauren"
			valid_races[6] = "gnome"
			valid_races[7] = "troll"
			valid_classes= numpy.empty(9, dtype=numpy.object)
			valid_classes[0]= "warrior"
			valid_classes[1]= "paladin"
			valid_classes[2]= "hunter"
			valid_classes[3]= "rogue"
			valid_classes[4]= "priest"
			valid_classes[5]= "shaman"
			valid_classes[6]= "mage"
			valid_classes[7]= "warlock"
			valid_classes[8]= "druid"
			rand1 = numpy.random.randint(9)
			if rand1 == 0:
				choice_list = [0, 1, 2, 3, 4, 5, 6, 7]
				rand2 = random.choice(choice_list)
			if rand1 == 1:
				choice_list = [0, 2]
				rand2 = random.choice(choice_list)
			if rand1 == 2:
				choice_list = [2, 1, 3, 7, 5]
				rand2 = random.choice(choice_list)
			if rand1 == 3:
				choice_list = [0, 1, 2, 3, 4, 6, 7]
				rand2 = random.choice(choice_list)
			if rand1 == 4:
				choice_list = [0, 2, 3, 4, 7]
				rand2 = random.choice(choice_list)
			if rand1 == 5:
				choice_list = [2, 5, 7]
				rand2 = random.choice(choice_list)
			if rand1 == 6:
				choice_list = [0, 6, 4, 7]
				rand2 = random.choice(choice_list)
			if rand1 == 7:
				choice_list = [0, 6, 2, 4]
				rand2 = random.choice(choice_list)
			if rand1 == 8:
				choice_list = [3, 5]
				rand2 = random.choice(choice_list)

			randrace = valid_races[rand2]
			randclass = valid_classes[rand1]
			self.absolute_final_result = (randrace, randclass)


	def calculate_final_result(self):
		base_matrix = numpy.asarray(self.base_values, dtype=numpy.float32)
		question_array = numpy.asarray(self.question_result, dtype=numpy.float32)
		print(base_matrix)
		print("_____________")
		print(question_array)
		print("_____________")
		print("go")

		weighted_response = base_matrix * question_array

		print("go")

		#sum alliance collumn
		alliance_sum = numpy.sum(weighted_response[17,:])
		horde_sum = numpy.sum(weighted_response[18,:])

		#multiply each alliance race column by the sum of the alliance column
		weighted_response[0,:] = weighted_response[0,:] * alliance_sum
		weighted_response[2,:] = weighted_response[2,:] * alliance_sum
		weighted_response[3,:] = weighted_response[3,:] * alliance_sum
		weighted_response[6,:] = weighted_response[6,:] * alliance_sum

		weighted_response[1,:] = weighted_response[1,:] * horde_sum
		weighted_response[4,:] = weighted_response[4,:] * horde_sum
		weighted_response[5,:] = weighted_response[5,:] * horde_sum
		weighted_response[7,:] = weighted_response[7,:] * horde_sum
		#multiply each horde race column by the sum of the horde column
		warrior_sum = numpy.sum(weighted_response[8,:])
		paladin_sum = numpy.sum(weighted_response[9,:])
		hunter_sum = numpy.sum(weighted_response[10,:])
		rogue_sum = numpy.sum(weighted_response[11,:])
		priest_sum = numpy.sum(weighted_response[12,:])
		shaman_sum = numpy.sum(weighted_response[13,:])
		mage_sum = numpy.sum(weighted_response[14,:])
		warlock_sum = numpy.sum(weighted_response[15,:])
		druid_sum = numpy.sum(weighted_response[16,:])

		#sum each race column
		#sum each class column

		human_sum = numpy.sum(weighted_response[0,:])
		orc_sum = numpy.sum(weighted_response[1,:])
		dwarf_sum = numpy.sum(weighted_response[2,:])
		nightelf_sum = numpy.sum(weighted_response[3,:])
		undead_sum = numpy.sum(weighted_response[4,:])
		tauren_sum = numpy.sum(weighted_response[5,:])
		gnome_sum = numpy.sum(weighted_response[6,:])
		troll_sum = numpy.sum(weighted_response[7,:])



		races_sums = [(human_sum,"0"), (orc_sum,"1"), (dwarf_sum,"2"), (nightelf_sum, "3"), (undead_sum, "4"), (tauren_sum, "5"), (gnome_sum, "6"), (troll_sum, "7")]
		classes_sums = [(warrior_sum, "0"), (paladin_sum, "1"), (hunter_sum, "2"), (rogue_sum, "3"), (priest_sum, "4"), (shaman_sum,"5"), (mage_sum, "6"), (warlock_sum, "7"), (druid_sum, "8")]



		final_races_results = numpy.asarray(races_sums, dtype=numpy.float32)
		final_classes_results = numpy.asarray(classes_sums, dtype=numpy.float32)



		best_match_race = numpy.amax(final_races_results[:,0], axis= 0)
		best_match_class = numpy.amax(final_classes_results[:,0], axis= 0)



		best_race = numpy.where(final_races_results == best_match_race)
		best_class = numpy.where(final_classes_results == best_match_class)

		print("go")

		print("go")



		try: 
			bc_val = int(best_class[0])
		except:
			bc_val = int(best_class[0][0])

		print("go")
		#bc_name = int(best_class[1])

		#get the Best Class
		bc_final = final_classes_results[bc_val,1]

		#check for best class 
		if bc_final == 0: #warrior
			bc_final_string = "warrior"
			#create new races array with only the valid races
			valid_races = numpy.empty([8,2])
			valid_races[0,:] = final_races_results[0,:] #human
			valid_races[1,:] = final_races_results[1,:] #orc
			valid_races[2,:] = final_races_results[2,:] #dwarf
			valid_races[3,:] = final_races_results[3,:] #ne
			valid_races[4,:] = final_races_results[4,:] #undead
			valid_races[5,:] = final_races_results[5,:] #tauren
			valid_races[6,:] = final_races_results[6,:] #gnome
			valid_races[7,:] = final_races_results[7,:] #troll
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			if br_final == 0: #human
				br_final_string = "human"
				absolute_final_result = (br_final_string, bc_final_string)		
			if br_final == 1: #orc
				br_final_string = "orc"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 2: #dwarf
				br_final_string = "dwarf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 3: #nightelf
				br_final_string = "nightelf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 4: #undead
				br_final_string = "undead"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 5: #tauren
				br_final_string = "tauren"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 6: #gnome
				br_final_string = "gnome"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 7: #troll
				br_final_string = "troll"
				absolute_final_result = (br_final_string, bc_final_string)

		if bc_final == 1: #paladin
			bc_final_string = "paladin"
			#create new array with valid races
			valid_races = numpy.empty([2,2])
			valid_races[0,:] = final_races_results[0,:]
			valid_races[1,:] = final_races_results[2,:]
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			print("go")
			if br_final == 0: #human
				br_final_string = "human"
				absolute_final_result = (br_final_string, bc_final_string)	
			if br_final == 2: #dwarf
				br_final_string = "dwarf"
				absolute_final_result = (br_final_string, bc_final_string)


		if bc_final == 2: #hunter
			bc_final_string = "hunter"
			#create new array with valid races
			valid_races = numpy.empty([5,2])
			valid_races[0,:] = final_races_results[1,:] #orc
			valid_races[1,:] = final_races_results[2,:] #dwarf
			valid_races[2,:] = final_races_results[3,:] #ne
			valid_races[3,:] = final_races_results[5,:] #tauren
			valid_races[4,:] = final_races_results[7,:] #troll
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			print("go")
			if br_final == 1: #orc
				br_final_string = "orc"
				absolute_final_result = (br_final_string, bc_final_string)	
			if br_final == 2: #dwarf
				br_final_string = "dwarf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 3: #ne
				br_final_string = "nightelf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 5: #tauren
				br_final_string = "tauren"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 7: #troll
				br_final_string = "troll"
				absolute_final_result = (br_final_string, bc_final_string)



		if bc_final == 3: #rogue
			bc_final_string = "rogue"
			#create new array with valid races
			valid_races = numpy.empty([7,2])
			valid_races[0,:] = final_races_results[0,:] #human
			valid_races[1,:] = final_races_results[1,:] #orc
			valid_races[2,:] = final_races_results[2,:] #dwarf
			valid_races[3,:] = final_races_results[3,:] #ne
			valid_races[4,:] = final_races_results[4,:] #undead
			valid_races[5,:] = final_races_results[6,:] #gnome
			valid_races[6,:] = final_races_results[7,:] #troll
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			if br_final == 0: #human
				br_final_string = "human"
				absolute_final_result = (br_final_string, bc_final_string)		
			if br_final == 1: #orc
				br_final_string = "orc"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 2: #dwarf
				br_final_string = "dwarf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 3: #nightelf
				br_final_string = "nightelf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 4: #undead
				br_final_string = "undead"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 6: #gnome
				br_final_string = "gnome"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 7: #troll
				br_final_string = "troll"
				absolute_final_result = (br_final_string, bc_final_string)
		if bc_final == 4: #priest
			bc_final_string = "priest"
			#create new array with valid races
			valid_races = numpy.empty([5,2])
			valid_races[0,:] = final_races_results[0,:] #human
			valid_races[1,:] = final_races_results[2,:] #dwarf
			valid_races[2,:] = final_races_results[3,:] #ne
			valid_races[3,:] = final_races_results[4,:] #undead
			valid_races[4,:] = final_races_results[7,:] #troll
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			if br_final == 0: #human
				br_final_string = "human"
				absolute_final_result = (br_final_string, bc_final_string)		
			if br_final == 2: #dwarf
				br_final_string = "dwarf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 3: #nightelf
				br_final_string = "nightelf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 4: #undead
				br_final_string = "undead"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 7: #troll
				br_final_string = "troll"
				absolute_final_result = (br_final_string, bc_final_string)
		if bc_final == 5: #shaman
			bc_final_string = "shaman"
			#create new array with valid races
			valid_races = numpy.empty([3,2])
			valid_races[0,:] = final_races_results[1,:] #orc
			valid_races[1,:] = final_races_results[5,:] #tauren
			valid_races[2,:] = final_races_results[7,:] #troll
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			if br_final == 1: #orc
				br_final_string = "orc"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 5: #tauren
				br_final_string = "tauren"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 7: #troll
				br_final_string = "troll"
				absolute_final_result = (br_final_string, bc_final_string)
		if bc_final == 6: #mage
			bc_final_string = "mage"
			#create new array with valid races
			valid_races = numpy.empty([4,2])
			valid_races[0,:] = final_races_results[0,:] #human
			valid_races[1,:] = final_races_results[4,:] #undead
			valid_races[2,:] = final_races_results[6,:] #gnome
			valid_races[3,:] = final_races_results[7,:] #troll
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			if br_final == 0: #human
				br_final_string = "human"
				absolute_final_result = (br_final_string, bc_final_string)		
			if br_final == 4: #undead
				br_final_string = "undead"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 6: #gnome
				br_final_string = "gnome"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 7: #troll
				br_final_string = "troll"
				absolute_final_result = (br_final_string, bc_final_string)
		if bc_final == 7: #warlock
			bc_final_string = "warlock"
			#create new array with valid races
			valid_races = numpy.empty([4,2])
			valid_races[0,:] = final_races_results[0,:] #human
			valid_races[1,:] = final_races_results[1,:] #orc
			valid_races[2,:] = final_races_results[4,:] #undead
			valid_races[3,:] = final_races_results[6,:] #gnome
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			if br_final == 0: #human
				br_final_string = "human"
				absolute_final_result = (br_final_string, bc_final_string)		
			if br_final == 1: #orc
				br_final_string = "orc"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 4: #undead
				br_final_string = "undead"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 6: #gnome
				br_final_string = "gnome"
				absolute_final_result = (br_final_string, bc_final_string)

		if bc_final == 8: #druid
			bc_final_string = "druid"
			#create new array with valid races
			valid_races = numpy.empty([2,2])
			valid_races[0,:] = final_races_results[3,:] #ne
			valid_races[1,:] = final_races_results[5,:] #tauren
			best_valid_race_max = numpy.amax(valid_races[:,0], axis= 0)
			best_valid_race = numpy.where(valid_races == best_valid_race_max)
			try: 
				br_val = int(best_valid_race[0])
			except:
				br_val = int(best_valid_race[0][0])
			br_final = valid_races[br_val,1]
			if br_final == 3: #nightelf
				br_final_string = "nightelf"
				absolute_final_result = (br_final_string, bc_final_string)
			if br_final == 5: #tauren
				br_final_string = "tauren"
				absolute_final_result = (br_final_string, bc_final_string)

		self.absolute_final_result = absolute_final_result

	def report(self):
		return self.absolute_final_result

	def gen_key(self):
		letters = string.ascii_lowercase
		numbers = string.digits

		x = ( ''.join(random.choice(numbers) for i in range(5)) )
		y = ( ''.join(random.choice(letters) for i in range(5)) )
		z = x + y

		return z


data = Singleton()
start = Interface()
start.main()
print("go")