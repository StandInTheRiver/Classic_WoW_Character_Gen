import numpy

warrior_sum = "500"
paladin_sum = "500"
hunter_sum = "500"
rogue_sum = "50"
priest_sum = "50"
shaman_sum = "50"
mage_sum = "50"
warlock_sum = "50"
druid_sum = "50"

human_sum = "500"
orc_sum = "500"
dwarf_sum = "500"
nightelf_sum = "50"
undead_sum = "50"
tauren_sum = "50"
gnome_sum = "50"
troll_sum = "50"

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

print(best_class[0])
print(best_class[0][0])
print(best_class[0][1])

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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
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
		br_val = int(best_race[0])
	except:
		br_val = int(best_race[0][0])
	br_final = valid_races[br_val,1]
	if br_final == 3: #nightelf
		br_final_string = "nightelf"
		absolute_final_result = (br_final_string, bc_final_string)
	if br_final == 5: #tauren
		br_final_string = "tauren"
		absolute_final_result = (br_final_string, bc_final_string)



print("the result of all this n onsense is that you picked")
print(absolute_final_result)