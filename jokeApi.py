import requests, json

'''
categories - 
    Programming
    Misc
    Dark
    Pun
    Spooky
    Christmas
'''

response = requests.get("https://v2.jokeapi.dev/joke/Misc")
#print(response)

#if the webpage of the word defintition actually exists
if response.status_code == 200:
    #stealing all the data from a web page
    apiData = json.loads(json.dumps(response.json()))

    #print(apiData)
    try:

        print(apiData["joke"])
    except KeyError:
        input(apiData["setup"])
        print(apiData["delivery"])
else:
    print("Error")