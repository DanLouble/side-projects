import random, time

maxNumber = 150 # Possible numbers on the card range from 1 to this number, inclusive
sideLength = 10# Cards will be a square with side length of this number

#Generate a list of numbers (stored as strings)
numberlist = []
for i in range(1, maxNumber + 1):
    numberString = str(i)
    #Add spaces to the beginning to keep all the numbers aligned
    while len(numberString) < len(str(maxNumber)):
        numberString = " " + numberString
    numberlist.append(numberString)
bingoMark = " " * (len(str(maxNumber)) - 1) + "●" # Add spaces to the bingo mark

#Class for each of the players
class Player:

    def __init__(self, name, numberlist):
        self.name = name
        self.numberlist = numberlist
        self.card = []

        #Generate a random bingo card
        for i in range(sideLength):
            row = []
            for j in range(sideLength):
                number = random.choice(self.numberlist)
                row.append(number)
                self.numberlist.remove(number)
            self.card.append(row)
        
        #If the side length is odd, make the middle space a Free Space
        if sideLength % 2 == 1:
            self.card[sideLength // 2][sideLength // 2] = bingoMark
    
    def displayCard(self):
        print(self.name + "'s Card")
        for eachRow in self.card:
            print(*eachRow)
        print()
    
    def crossNumber(self, number):
        for i in range(sideLength):
            for j in range(sideLength):
                #If the number is present on the card, replace it with '●'
                if self.card[i][j] == number:
                    self.card[i][j] = bingoMark

    def checkForRow(self):
        #Check for horizontal row - if all rows are filled in at any given index
        for eachRow in self.card:
            if all(eachNum == bingoMark for eachNum in eachRow):
                return True
        
        #Check for vertical row - if all of any given row is filled in
        for i in range(sideLength):
            if all(eachRow[i] == bingoMark for eachRow in self.card):
                return True

        #Check for diagonal row - if [0][0], [1][1], etc. are all filled in OR if [0][-1], [1][-2] etc. are all filled in
        if all(self.card[i][i] == bingoMark for i in range(sideLength)) or all(self.card[i][-1 - i] == bingoMark for i in range(sideLength)):
            return True



#Get valid input for the number of players
valid = False
while not valid:
    try:
        numberOfPlayers = int(input("How many players? "))
    except ValueError:
        print("Invalid, must be a number")
        continue
    if numberOfPlayers < 1:
        print("Invalid, must be a positive number")
        continue
    valid = True

#Instansiate the players
players = []
for i in range(numberOfPlayers):
    players.append(Player(input("What is your name? "), numberlist[:]))
    players[i].displayCard()

winners = []
playing = True
#Main game loop
while playing:

    #Pick a number
    number = random.choice(numberlist)
    #number = input("Enter the number: ") # Debug line
    numberlist.remove(number)
    print("The number is " + str(number))
    time.sleep(1)

    #Cross off the number on the players cards
    for i in range(numberOfPlayers):
        players[i].crossNumber(number)
        players[i].displayCard()
        if players[i].checkForRow() == True:
            playing = False
            winners.append(players[i].name)

#Display who the winners are
if len(winners) == 1:
    print(winners[0], "got a BINGO!")
else:
    print(", ".join(each_winner for each_winner in winners[:-1]), "and", winners[-1], "got a BINGO!")