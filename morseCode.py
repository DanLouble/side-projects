from gpiozero import Button, Buzzer
import time

#setting what gpiopins, the sensors are on
button = Button(3)
buzzer = Buzzer(4)

#initialising arrays to use later on
sequence = []
wordList = []
sentenceList = []

#function to choose which character to write
#takes in the sequence of button presses and the beep time duration vs letter conversion list
def beepDeterminer(sequence, letterDic):
    #finds if the sequence created is within the letter list
    if tuple(sequence) in letterDic:
        #add the letter of the sequence to a word list
        wordList.append(letterDic[tuple(sequence)])
        #display contents of the word list
        print(*wordList)

#initialising start and finish times to be used later in the loop
start, finish = time.time(), time.time()

#defining what happens when the button is pressed
def buzzOn():
    global start
    #starting the start timer
    start = time.time()
    #turning the buzzer on
    buzzer.on()

#defining what happens when the button is released
def buzzOff():
    global finish, timeOff
    #taking a finish time
    finish = time.time()
    #turning the buzzer off
    buzzer.off()
    #displaying the duration of how long the button was pressed for to help keep track of sequence
    print(timePressed)
    
    #adding short or long value to the sequence depending on how long the button was pressed for
    if 0.05 <= timePressed <= 0.125:
        sequence.append(short)
    elif 0.25 <= timePressed <= 0.35:
        sequence.append(long)

#to help with clarity of any loops that may appear after adding the wordlist to the sentencelist
def duplicateWords(sentencelist):
    normal = []
    for i in range(len(sentencelist)):

        if i == 0 or sentencelist[i] != sentencelist[i -1]:
            normal.append(sentencelist[i])
    print("sentence list -"," ".join(normal))

#selector variables
short = 0.1
long = 0.3

#sequence converting list
letterDic = {

    (short, long): "a",
    (long, short, short, short): "b",
    (long, short, long, short): "c",
    (long, short, short): "d",
    (short,): "e",
    (short, short, long, short): "f",
    (long, long, short): "g",
    (short, short, short, short): "h",
    (short, short): "i",
    (short, long, long, long): "j",
    (long, short, long): "k",
    (short, long, short, short): "l",
    (long, long): "m",
    (long, short): "n",
    (long, long, long): "o",
    (short, long, long, short): "p",
    (long, long, short, long): "q",
    (short, long, short): "r",
    (short, short, short): "s",
    (long,): "t",
    (short, short, long): "u",
    (short, short, short, long): "v",
    (short, long, long): "w",
    (long, short, short, long): "x",
    (long, short, long, long): "y",
    (long, long, short, short): "z",
}

try:
    print("Morse code translation: ") 
    
    #stating the on and off roles of the button
    button.when_pressed = buzzOn
    button.when_released = buzzOff
    #timeOff = round((time.time() - finish),2)
    while True:
        #takes a duration of press
        timePressed = round((time.time() - start),2)
        #takes a duration of time between now and last time pressed
        timeOff = round((time.time() - finish),2)

        #ending the loop if no activity after 5 seconds
        if timeOff >= 5:
            break
        #submitting sequence to beep finding function
        if 0.5 < timeOff <= 1 and 0 < len(sequence) <=4:
            beepDeterminer(sequence, letterDic)
            #resetting the sequence for next sequence
            sequence = [] 

        #moving word to sentence list and restarting to form another word
        elif 1 < timeOff <= 2:
            sentenceList.append("".join(wordList))
            wordList = []
            sequence = []

    duplicateWords(sentenceList)
    print("Morse code translator Over.")

#providing suitable error message if you ctrl+c out the program without waiting the 5 second delay
except KeyboardInterrupt:
    print("\nMorse code translator Over.")
