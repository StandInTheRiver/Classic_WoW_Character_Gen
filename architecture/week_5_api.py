import requests #api wrapper module


#sends api request to url
api_response = requests.get("http://api.icndb.com/jokes/random?limitTo=nerdy")
#when you make a request, you get http headers (meta data) about the request


#show the response in text format
print ("raw response is" + api_response.text)



#converts the response into json object
api_dict = api_response.json()


#this is a pointer = go to value, find joke, output that
print("the joke is " + api_dict["value"]["joke"])


print("go")

#making a request with specific paramaters
api_param = {"firstName":"Stephen","lastName":"dybka","limitTo":"nerdy"}
api_response2 = requests.get("http://api.icndb.com/jokes/random",api_param)

#printing the json response in one line
print ("raw response 2" + api_response2.json()["value"]["joke"] + "\n")


print("go")


#for api's that requires a key

key = "Y4ezhsaXmM_FxV6KAyPY" #key name
water_param = {"access_token":key} #parameter object
str = "https://api.onwater.io/api/v1/results/43.2609,-79.9192" #request string
mcmaster_response = requests.get(str,water_param) #call the request to the api string given the parameters
print(mcmaster_response.text) #print response



#wrapper example
#sometimes we use a wrapper - much easier, we dont work with raw request response data

#pip install the wrapper
#import the wrapper
#use the wrapper as needed
#each wrapper has its own syntax

