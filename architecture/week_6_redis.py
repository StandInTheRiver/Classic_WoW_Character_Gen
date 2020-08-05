import redis

r = redis.Redis(
	host="redis-14585.c11.us-east-1-3.ec2.cloud.redislabs.com",
	port="14585",
	password="TMgOol2qM6wjkypZ1qrbaovjJcRXTpy2",
	decode_responses=True
)


#show connection info
print(r)


#set a key and get a key than print it
#by default returns binary format string, include decode_reponses to remove
r.set("test_key","test_value")
value = r.get("test_key")
print (value)

r.set("test_key2","test_value2")
value2 = r.get("test_key2")
print (value2)




#create hash list
r.hset("hashkey", "hashfield1", "hashvalue1")
r.hset("hashkey", "hashfield2", "hashvalue2")
r.hset("hashkey", "hashfield3", "hashvalue3")

#get all from the hashlist
result = r.hgetall("hashkey")
print(result)

#get one value from a field in a hashkey
result2 = hash_val = r.hget("hashkey","hashfield1")
print(result2)


