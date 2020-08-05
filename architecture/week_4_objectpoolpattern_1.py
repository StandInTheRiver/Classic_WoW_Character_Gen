#using sqllite - just a file on the filesystem
import timeit #timing library for code execution
import sqlite3 #db 



#version 1 of code
#using no pattern

#defining a function
def create_and_destroy_resource():
	for i in range(5000): #do this 5000 times
		conn = sqlite3.Connection("stocks2.db") #create connection to the file
		conn.execute("DROP TABLE IF EXISTS stocks") #destroy table if it exists
		conn.commit() #commit sql changes
		conn.execute("Create TABLE stocks (symbol text, price real)") #create the table
		conn.execute("INSERT INTO stocks VALUES ('RHAT', 35.24)") #add a value to the table
		conn.commit()
		conn.close()

#run the function one time, and time it saving it in testcreatedestroy
#testCreateDestroy = timeit.timeit(create_and_destroy_resource, number=1)
#print("create and destroy resource: " + str(testCreateDestroy) + "s")

#version 2 of code
#using object pool pattern

class Reusable:

    # create the connection
    def __init__(self, database_to_open):
        self.conn = sqlite3.connect(database_to_open)

    # close the connection when the object is deleted
    def __del__(self):
        self.conn.close()


class ObjectPool:

    # initialize the pool... in our case, just one re-usable object
    def __init__(self):
        self.__reusables = [ Reusable("stocks1.db") ]

    # give the resource to a client
    def acquire(self):
        return self.__reusables.pop()

    # accept the resource back from a client
    def release(self, reusable):
        self.__reusables.append(reusable)



#client code for object pool

def object_pool_pattern():
    pool = ObjectPool()
    for i in range(5000):
        db = pool.acquire()
        db.conn.execute("DROP TABLE IF EXISTS stocks")
        db.conn.commit()
        db.conn.execute("CREATE TABLE stocks (symbol text, price real)")
        db.conn.execute("INSERT INTO stocks VALUES ('RHAT',35.14)")
        db.conn.commit()
        pool.release(db)



#run the function one time, and time it saving it in testcreatedestroy
testObjectPool = timeit.timeit(object_pool_pattern, number=1)
print("object pool pattern: " + str(testObjectPool) + "s")