import threading
from queue import Queue
from random import random
from time import sleep
import timeit
from concurrent.futures import ThreadPoolExecutor
import numpy

def task():

	sleep(0.0001)
	print("task completed")


def execute():

	threadpool = ThreadPoolExecutor(max_workers=500)

	x = 10
	y = numpy.empty(x, dtype=object)
	k =  0
	for i in range(0,x):
		print(i)
		y[i] = threadpool.submit(task)
		#threadpool.submit(task)
		print("done")
		print (y[i]._state)
	print(y)

	while k != x:
		for i in range(0,x):		
			if y[i]._state == "FINISHED":
				print("state finished")
				k = k + 1
			else:
				return
		


test = timeit.timeit(execute, number=1)
print("Test result: " + str(test) + "s")

print("go")