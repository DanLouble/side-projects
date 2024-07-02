import requests, json

name = input("what is the name you want to guess the age of? ")

response = requests.get("https://api.agify.io?name=" + name)
#print(response)

#if the webpage of the word defintition actually exists
if response.status_code == 200:
    #stealing all the data from a web page
    apiData = json.loads(json.dumps(response.json()))
    
    print(apiData["age"])