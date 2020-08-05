#comment

#PROGRAM CODE

#concrete objects = objects you can actually create
#no such thing as a generic student however...
#polymorphism = when children have methods from parents
#abstract types = objects that 

class Student: #define a class called "student"

	#class variables belong to the actual class, not each instance of the class
	next_id = 1 #next_id is a class variable, defined as 1 here in this case


	#creates a class method called student_id_range
	@classmethod #known as a decorator
	def student_id_range(cls):
		return range(cls.next_id)

	#cls = the classes self
	#self = the object itself
	def __init__(self,first_name,last_name,grades): #creates the constructor known as "init", giving it, self,lastname,firstname,grades as instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.grades = grades
		self.__student_id = Student.next_id # putting __ infront of an instance variable makes it private, this is not accessible when creating a class object, it cannot be referenced
		Student.next_id = Student.next_id + 1 #increments the student ID everytime a new object is created
		#we set the grades data for the student class equal to its respective thing

	def average(self): #this defines the method named average for the object
		return sum(self.grades) / len(self.grades) #takes the sum of grades divided by the length of grades

	def honors(self): #defining the method called honors
		if self.average() > 80: return True #computes average for self, if its g reater than 80 returns true
		else: return False #if less than 80, returns false




class GraduateStudent(Student): #defining a new class called graduatestudent, which is a student (INHERITENCE)

	#overriding the st udent initializer because we now have an extra instance variable called thesis
	def __init__(self,first_name,last_name,grades,thesis): #redefining the constructor for a graduatestudent to include thesis instance variable
		super().__init__(first_name,last_name,grades) # "get the methods in the super object (student in this case), than call init and feed it the three things
		self.thesis = thesis


class MedicalStudent(Student):

	#overide the honors method from student by making it now require a 90 for honors to be true for medical students
	def honors(self):
		if self.average() > 90: return True
		else: return False

class Course:

	def __init__(self,name,students):
		self.name = name
		self.__students = students




#CLIENT CODE



#create two student objects, the class variables are positional
steve = Student("steve", "dybka", [60,70,80]);
chris = Student("chris", "dybka", [50,90,100]);
zenek = GraduateStudent("zenek", "dybka", [50,100,100], "advanced microbiology");
guad = Student("guad", "man", [20,20,45]);
maria = MedicalStudent("maria", "dybka", [90,100,99]);
brian = MedicalStudent("brian", "juliao", [80,83,81]);


#create an array called studentlist with the contents including our objects
studentlist = [steve, chris, zenek, guad, maria, brian];
for student in studentlist:
	print (student.first_name + " " + student.last_name + str(student.average())) #print stuff requested for each object


for student in studentlist:
	print(student.first_name + " " + ("honors" if student.honors() else "not honors")) #inline logic, printing the first stuff everytime, changing honors if true or false returns from calling the object method honors()

#print(steve.student_id); #this will not work since its private
print(steve._Student__student_id) #this will show it, but you shouldnt do this 
print(chris._Student__student_id) #this will show it, but you shouldnt do this 
print(steve.last_name); #shows us the student object named steves last name
print(chris.grades); #shows us the student object named chris's grades
print(Student.next_id); #shows the student ID
print(steve.average()); #when calling a method we must use the name() with the brackets to actually call it to activate
print(chris.average());
print(zenek.thesis);
print(guad.honors());
print(zenek.honors());

print("start");


math = Course("math", studentlist);

print(math.name);


print("finish");