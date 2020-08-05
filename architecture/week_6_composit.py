from abc import ABC, abstractmethod


#create abstract class called component
class Component(ABC):

	@abstractmethod
	def size(self, components):
		pass


	#file component has a name and size
class File(Component):

	def __init__(self, name, size):
		self.__name = name
		self.__size = size

		#size method returns size
	def size(self):
		return self.__size

	#folder component
class Folder(Component):

	#foldres have a name and components
	def __init__(self, name, components):
		self.__name = name
		self.__components = components

		#for calculating size, we take all the components and call there size function and add them
	def size(self):
		total = 0
		for component in self.__components:
			total = total + component.size()
		return total


#Client code
myfile = File("name1", 45)

print (myfile.size())

myfolder = Folder("documentsfolder", [File("resume", 500), File("pictures", 250) ] )

print(myfolder.size())



desktop = Folder("desktop", [File("img1", 5325), File("dog2", 23532)])
desktop2 = Folder("desktop", [File("img1", 5325), File("dog2", 23532)])
desktop3 = Folder("desktop", [File("img1", 5325), File("dog2", 23532)])
desktop4 = Folder("desktop", [File("img1", 5325), File("dog2", 23532)])


newfolder = Folder("newfolder", [desktop, desktop2, desktop3, desktop4, File("steve", 10), File("ya", 233)])

print(newfolder.size())