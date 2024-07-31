import time

#alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#place to store any untyped letters
missedLetters = []

#place to store letters in incorrect positions
misplacedLetters = []

#place to store any duplicates
repeatedLetters = []

#matthew's duplicate' duplicate remover (it removes extra letters of the same from the duplicate list)
def removeDuplicates(localArray):
    outputArray = []
    for eachChar in localArray:
        if not eachChar in outputArray:
            outputArray.append(eachChar)
    #localArray.sort()
    return localArray





input("type the alphabet as fast as you can after pressing enter ")

#starting the timer
start = time.time()
attempt = input(": ")



end = time.time()

#final time
timer = round(end-start,1)

#printing any recurring letters
#for i in range(len(attempt)):
#    if attempt[i] in attempt[(i+1):]:
#        print("You repeated " + attempt[i])
#        repeatedLetters.append(attempt[i])

#loop to check how you scored
for i in range(len(alphabet)):
    

    try:
        if attempt[i] == alphabet[i]:
            pass
        else:
            attempt.replace(attempt[i],"_")
            missedLetters.append(alphabet[i])


    except IndexError:
        attempt += "_"
        missedLetters.append(alphabet[i])

for eachcharacter in attempt:
    
    if eachcharacter in alphabet and alphabet.index(eachcharacter) != attempt.index(eachcharacter) :
        misplacedLetters.append(eachcharacter)


for eachcharacter in misplacedLetters:
    if eachcharacter in missedLetters:
        missedLetters.remove(eachcharacter)

misplacedLetters = sorted(misplacedLetters)
repeatedLetters = removeDuplicates(repeatedLetters)

if len(missedLetters) == 0:
    missedLetters.append("none")
elif len(misplacedLetters) == 0:
    misplacedLetters.append("none")
elif len(repeatedLetters) == 0:
    repeatedLetters.append("none")
#elif len(misplacedLetters) > 0:
#    misplacedLetters.append("no letters and")
print(attempt)
#print(len(repeatedLetters))


if list(attempt) == alphabet and timer <= 20:
    print("congratulations, you won in",timer,"seconds")
elif list(attempt) != alphabet:
    print("sorry bozo try again, you missed out:", *missedLetters)
    print("repeated:", *repeatedLetters)
    print("misplaced letters:",*misplacedLetters)
else:
    print("nuh uh, you typed it correctly but only in", timer,"seconds")    
    

