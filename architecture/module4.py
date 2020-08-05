import random
import string
import numpy

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
result = (randrace, randclass)
print(result)
print("go")