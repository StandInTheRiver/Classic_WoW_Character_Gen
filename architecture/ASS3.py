################################################################################
# Assignment #3 Factory Pattern Starter Code
#
# Starter code for Assignment #3...
#
# The Open Weather Map API allows to to request the weather for a given city:
#   - Documentation: https://openweathermap.org/api
# In order to use this API, we do need to create an account to obtain an API
# key: https://home.openweathermap.org/users/sign_in.  And it does take a few
# minutes for the API key to start working after we've signed up for it...
#
# This API also has a "wrapper", a Python module that makes accessing the API
# easier for us... rather than manually making and sending requests, we
# can call functions that do this for us and just return the results.
#  - Wrapper documentation: https://github.com/csparpa/pyowm
#
# See the WebAPI Examples on Avenue for an example of using this wrapper!
#
# To install a Python module locally to make it available in your own solutions,
# you generally need to use pip3:
#    pip3 install pylast
#

# import the open weather data wrapper module
from pyowm import OWM #module wrapper for weather api from github
from abc import ABC, abstractmethod #abstract method class from python

owm = OWM('3ab86c7fb35485b4a7f1dea3fa31703f') #setting my key in the wrapper
mgr = owm.weather_manager() #creating weather manager object from wrapper


# Implement these classes: Factory, WeatherData, Wind, Humidity, Temperature

class WeatherData(ABC): #abstrat class called weatherdata derived from ABC

    @abstractmethod #defining an abstract method to be used in each child object created from this abstract class
    def output():
        pass #do nothing

    def __init__(self, location): #on creation set the location to self for the weatherdata object
       self.location = location
        


class Wind(WeatherData): #class called wind which is a child object of weatherdata, it inherits all its stuff

    def __init__(self, location, wind_speed): #Takes a location and a wind_speed as input
        super().__init__(location) #this location is already defined in the super class so we call that method instead passing it location
        self.wind_speed = wind_speed #set self to windspeed for this object

    def output(self): #method called output
        print ("the wind speed is: " + str(self.wind_speed["speed"]) + "m/s" + " At location: " + self.location ) #outputs a string referencing things from its Init which are given to it by the factory
                                                    #python uses dictionaries, to reference the object in the dictionary you put [name] after the variable

class Temperature(WeatherData):

    def __init__(self, location, temperature):
        super().__init__(location)
        self.temperature = temperature

    def output(self):
        print ("the temperature in celcius is: " + str(self.temperature["temp"]) + " At location: " + self.location)

class Humidity(WeatherData):

    def __init__(self, location, humidity):
        super().__init__(location)
        self.humidity = humidity

    def output(self):
        print ("the humidity level is: " + str(self.humidity) + "%" + " At location: " + self.location)

class Factory(): #factory class


    def __init__(self): #on creation, setup two variables specific to each instance of the object factory
        self.x = [] #empty array
        self.count = 0 #integer starting at 0



    def createData(self, location, type): #createdata method, takes a location and a type
        self.location = location #sets the variables for the object
        self.type = type

        #if statements to check the type given by the user
        if self.type == "humidity":
            observation = mgr.weather_at_place(self.location) #call the weather manager wrapper giving it our location
            w = observation.weather #creates a temp object called w, it holds all the weather information for that location
            self.x.append(Humidity(self.location, w.humidity)) #adding a new object we create to the factories list of created objects, the object is given the location and the results of the wrapper api call
            self.count = self.count + 1 #increment our counter for the next object to be created
            return Humidity(self.location, w.humidity) #i included this as well, since your testing method requires objects to be created and "spat out" of the factory

        if self.type =="wind":
            observation = mgr.weather_at_place(self.location)
            w = observation.weather
            self.x.append(Wind(self.location, w.wind()))
            self.count = self.count + 1
            return Wind(self.location, w.wind())

        if self.type == "temperature":
            observation = mgr.weather_at_place(self.location)
            w = observation.weather
            self.x.append(Temperature(self.location, w.temperature('celsius')))
            self.count = self.count + 1
            return Temperature(self.location, w.temperature('celsius'))
        else:
            pass


############client code##################


#my testing data client code
factorytest = Factory() #create factory object
factorytest.createData("Hamilton,ON,CA", "humidity") #call the factory objects createdata method 3 times
factorytest.createData("Brantford,ON,CA", "wind")
factorytest.createData("Simcoe,ON,CA", "temperature")
#each time we call createdata method, a new object is created and appended to the factories "completed objects" list "x"

#for every object in the factories "created objects" list "x"
for object in factorytest.x:
    object.output() #call that objects Output method

print("space________________") #clarity

#repeat the same process to check to make sure that if we create a second factory - the factories list of created objects is distinct
factorytest2 = Factory()
factorytest2.createData("Kitchener,ON,CA", "humidity")
factorytest2.createData("Kingston,ON,CA", "wind")
factorytest2.createData("Guelph,ON,CA", "temperature")

for object in factorytest2.x:
    object.output()

print("go") #clairty and stop point to view live objects and memory for debugging





# Create factory object
factory = Factory()

# Create a WeatherData object of each type (Wind, Temperature, Humidity) at
# different locations so we can test our factory's createData instance method
weatherdata = [factory.createData("Hamilton,ON,CA","wind"), \
               factory.createData("Toronto,ON,CA","humidity"), \
               factory.createData("Ottawa,ON,CA","temperature")]

# Call the output method for each WeatherData object
for data in weatherdata:
    data.output()

# When I run the above code with my factory object and WeatherData objects
# implemented, I get the following:
#
#   Wind speed of 6.7 meter/sec in Hamilton,ON,CA
#   Humidity of 35% in Toronto,ON,CA
#   Temperature of 30.71C in Ottawa,ON,CA
#


