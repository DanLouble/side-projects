import random, math, requests, json

# Function checks if the string contains any special character


filename = "/usr/share/dict/british-english"


#variable that is assigned by grabbing words from the dictionary file 
DictionaryWords = ([x.strip().lower() for x in open(filename,"r")])


#list of words that make it past the filter stage (no special characters)
validwords = []

#list of words that don't make it past the filter stage such as "that's" due to the apostrophe
invalidwords = []

#loop to run until valid words has 100 items
for i in range(len(DictionaryWords)):

    #middle man list 
    specialCharactersChecker = []
    
    #temporarily holds words grabbed from the dictionary
    specialCharactersChecker.append(DictionaryWords[i])

    #converting the list item into a string
    newstring = (''.join(specialCharactersChecker))


    #checkpoint-works well up to here so far
    if newstring.isalpha() and 14 > len(newstring) > 4:
        #adding the grabbed word to the valid word list if it has no special characters
        validwords.append(newstring)
        #resetting the item string verifier
        newstring = newstring.replace('',newstring)
   
   #if the string verifier has a special character
    elif newstring.isalpha() == False:
        invalidwords.append(newstring)
        #resetting the item string verifier
        newstring = newstring.replace('',newstring)



#stages of lives left in ascending order

Graphics = [r'''
------------           ___    ___   _____     _     _        ____        _    ______    _____
|         |            | |    | |  / ____ \  | |   | |      | ___ \     | |  |  ____|  |  __ \   
|          O            \ \  / /  | |    | | | |   | |      | |  \ \    | |  | |       | |  \ \ 
|         / |            \ \/ /   | |    | | | |   | |      | |   \ \   | |  | |___    | |   \ \   
|          |              |  |    | |    | | | |   | |      | |    | |  | |  |  ___|   | |    | |  
|         / |             |  |    | |____| | | |___| |      | |____| |  | |  | |____   | |____| |  
|                         |__|     \______/   \_____/       |________|  |_|  |______|  |________|  ''',r'''
------------
|         |
|          O 
|         / |
|          |
|         / 
|          ''',r'''
------------
|         |
|          O 
|         / |
|          |
|          
|          ''',r'''
------------
|         |
|          O 
|         / |
|          
|          
|          ''',r'''
------------
|         |
|          O 
|         / 
|          
|          
|          ''',r'''
------------
|         |
|          O 
|         
|          
|          
|           ''',r'''
------------
|         |
|           
|         
|          
|          
|           ''',r'''
''',r'''
''',r'''
''',r'''
''']


#keeping a record of letters you've entered to validate any potential duplicates
enteredletterlist = []
wrongLetters = []

#random word picker
word = (random.choice(validwords)).lower()

#print(word)

#print(len(validwords))

#you figure it out I don't care anymore
guesslen = len(word)

#does what it says on the tin
totallives = math.ceil(50 / len(word))

#starting life message
print("you have",totallives,"lives or you die")

#hint determiner
hiddenword = ["_"]*len(word)
print(*hiddenword)

#Basically says while you haven't guessed the word and you haven't died, continue playing
while guesslen > 0 and totallives > 0:


    if len(wrongLetters) > 0:
        print("Incorrect letters: ", *wrongLetters)

    #guess inputer
    guess = input("guess a letter:").lower()

    #input validation to stop you from entering a key that is a duplicate, non-letter or multiple letters at a time
    while guess in enteredletterlist or guess.isalpha() == False or len(guess) > 1:
        if guess in enteredletterlist:
            print("you've already entered that letter")
            guess = input("guess another letter ")
        elif guess.isalpha() == False:
            guess = input("error, give me a letter this time: ")
        elif len(guess) > 1:
            guess = input("only one letter ")
    

    #keeps track of how many words you've guessed correct
    count = word.count(guess)


    #replacing the hidden letter in it's location if you guessed correct
    for i in range(len(word)):
        if guess == word[i]:

            hiddenword[i] = guess
        #else:
         #   for position, letter in enumerate(word):
          #      if letter == guess:
           #         hiddenword[position] = guess
    

    #sending every new letter to the non-duplicate list
    enteredletterlist.append(guess)
    

    #keep a life if you got a letter correct
    if count > 0 and guesslen > 0:
        guesslen -= count 
        print("correct!",totallives,"lives left")
    #lose a life if you're wrong
    else:
        totallives -= 1
        print("wrong, you have",totallives,"lives left")    
        wrongLetters.append(guess)
    

    #displaying the life state of the hangman depending on how many lives are left
    print(Graphics[totallives])

    #clue to help you guess the word is displayed
    print(*hiddenword)
    
#win message after the game is over.
if guesslen == 0:
    print("congratulations, hangman survives! The word is",word)
    if len(wrongLetters) == 0:
        print("Perfect game!!")

#lose message after you lost and hangman dies     
if totallives == 0:
    print(" ")
    print("you died. The word was",word)
    print(" ")
    if all(x == "_" for x in hiddenword):
        print("Awful game, you got NO letters right!!")
# if you wan t know the word meaning
response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
#print(response)

#if the webpage of the word defintition actually exists
if response.status_code == 200:
    #stealing all the data from a web page
    apiData = json.loads(json.dumps(response.json()))
    #apiData = json.loads(apiData)
    #print(apiData)

    try:
        #looking through each definition of the word
        for eachDefinition in apiData[0]["meanings"][0]["definitions"]:
            
            #for the first or only definition for a word
            if apiData[0]["meanings"][0]["definitions"].index(eachDefinition) == 0:
                question = input("do you want to know the meaning of " + word + "? ")
            #if there is more than one definition of a word
            else:
                question = input("do you want to know the next meaning of " + word + "? ")
            #printing the definition to the user in the termnial
            if question[0].lower() == "y":
                print(eachDefinition["definition"]+"\n")
            else:
                break
    except IndexError:
        pass

#if the definition webpage for the word doesn't exist
else:
    print("No meaning available.")