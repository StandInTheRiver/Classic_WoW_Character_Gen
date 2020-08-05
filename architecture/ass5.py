
################################################################################
# Thread pool pattern opportunity
#
# Purpose: The below code simulates a situation where we have "bursts" made up
# of some number of jobs that need to be done, where the precise number
# of jobs varies between 0-20 for each burst, and all the jobs in one burst
# must be completed before moving on to the next.  Completing a job is done
# by calling the do_job method.  The jobs can be run concurrently without any
# regard to race conditions.
#
# In the below code, we use multithreading to improve the performance of
# executing bursts of jobs.  There is an opportunity to use a thread pool
# instead.
#
#
# Author: Kevin Browne
# Contact: brownek@mcmaster.ca
#
################################################################################

import threading
from queue import Queue
from random import random
from time import sleep
import timeit
from concurrent.futures import ThreadPoolExecutor #included for using the threadpool c lass
import numpy

def do_job(output_queue,id):
    sleep(0.0001)
    output_queue.put(1)


def execute():
    BURSTS = 1000
    queue = Queue()
    threadpool = ThreadPoolExecutor(max_workers=50)

    for i in range(0, BURSTS):
        #print("burst" + str(i))
        job_total = int(round((random() * 20), 0))
        #print("total jobs for burst" + str(job_total))
#################################################################################
        y = numpy.empty(job_total, dtype=object) #create a numpy object array with size equal to total jobs
        #k = 0
        for j in range(0, job_total): #for each number in job total
            y[j] = threadpool.submit(do_job(queue, j)) #create a new threadpool object at array index = j, submit it the dojob method with queue and j as parameters
            

        #below is some code i was using to verify that each thread actually finished when it should have for testing
        #while k != job_total:
        #    for g in range(0,job_total):
        #        if y[g]._state == "FINISHED":                   
        #            k = k + 1
        #           print("burst: " + str(i)  + " job: " + str(g) + " state finished")
        #        else:
         #           return
#################################################################################   
#
#
         
    print(queue.qsize())


test = timeit.timeit(execute, number=1)
print("Test result: " + str(test) + "s")
