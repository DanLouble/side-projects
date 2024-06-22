import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

missedLetters = []

misplacedLetters = []


input("press enter to play ")
start = time.time()
attempt = input("type the alphabet ")



end = time.time()

timer = round(end-start,1)



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

if len(missedLetters) == 0:
    missedLetters.append("no letters but")
elif len(misplacedLetters) == 0:
    misplacedLetters.append("no letters")
#elif len(misplacedLetters) > 0:
#    misplacedLetters.append("no letters and")
print(attempt)

misplacedLetters = sorted(misplacedLetters)

if list(attempt) == alphabet and timer <= 10:
    print("congratulations, you won in",timer,"seconds")
elif list(attempt) != alphabet:
    print("sorry bozo try again, you missed out", *missedLetters ,"got",*misplacedLetters,"in the wrong place")
else:
    print("nuh uh, you typed it correctly but only in", timer,"seconds")    
    
