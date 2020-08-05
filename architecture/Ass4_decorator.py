################################################################################
# Assignment #4
#
# Purpose: The below code can be re-factored to use the Decorator pattern.
# Author: Kevin Browne
# Contact: brownek@mcmaster.ca
#
################################################################################



#i am really not sure if i Did this right, my understanding of the decorator pattern is that 
#instead of just chaining classes together to be subclasses and making new subclasses anytime we want to add new functionality
#we instead just create a decorator class, that takes any options at run time - and than calls the interface
#the interface determines which classes to call based on the options we feed it
#the classes themselves just print letters

#I'll try to comment below what im doing

class Interface: #this class is the "interface" its the only class that needs to be updated as you add more "features" or "options"

    def __init__(self, option):
        self.option = option #we get an option, and than we check that option against a list of known features

        if self.option == "A": #if the feature exists - we call that class to do what ever it does
            A.f()

        if self.option == "B":
            B.f()

        if self.option == "C":
            C.f()


class Decorator: #the client use this class to start the program at runtime - feeding it a list of options or "features"
    
    def __init__(self, option_array):
        self.option_array = option_array

        for item in self.option_array: #for each option or feature given, contact the interface class to do some work
            Interface(item)
            

#below are your classes, a b c that all print a b c , they now do not inherit anything and this list of features can be increased as new features are added
class A:
    def f():
        print("A")

class B:
    def f():
        print("B")

class C:
    def f():
        print("C")

#client code

#first you create an array with the features you want or options at run time
x = ["A", "B", "C", "C", "C"] #an example of letters 
#you than call the spell class giving it your feature list
testspell = Decorator(x)        
#the system than parses your list of features and instantiates or calls any that exist




print("go")


