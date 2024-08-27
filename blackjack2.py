import random, time
cardTypes = ["Hearts","Spades","Diamonds","Clubs"]

specialRanks = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King",
}

cardDeck = []
for eachsuit in cardTypes:
    for i in range(1, 14):
        if i in specialRanks:
            rank = specialRanks[i]
        else:
            rank = str(i)
        cardDeck.append((rank, eachsuit))

#print(cardDeck)

def balanceUpdater():

    
    with open("/home/danny/Desktop/vs code/BlackjackBalance.txt","w")as balanceFile:
        balanceFile.write(str(gamblingBalance))



with open("/home/danny/Desktop/vs code/BlackjackBalance.txt", "r") as balanceFile:
    gamblingBalance = int(balanceFile.read())
    if gamblingBalance <= 20:
        gamblingBalance += 100
        



class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def dealCard(self, numberOfCards):
        for i in range(numberOfCards):
            card = random.choice(cardDeck)
            self.hand.append(card)
            cardDeck.remove(card)

    def numberTotal(self):
        localTotal = 0
        aces = 0
        for eachCard in self.hand:
            if eachCard[0] == "Ace":
                localTotal += 11
                aces += 1
            elif eachCard[0] in ["Jack", "Queen", "King"]:
                localTotal += 10
            else:
                localTotal += int(eachCard[0])
        while aces > 0 and localTotal > 21:
            localTotal -= 10
            aces -= 0
        return localTotal


players = []
numberOfPlayers = int(input("How many players? "))
for i in range(numberOfPlayers):
    name = input("What is your name? ")
    players.append(Player(name))
players.append(Player("DEALER"))

winners = []

for playerNum in range(numberOfPlayers + 1):

    players[playerNum].dealCard(2)

    playing = True

    while playing:
        
        print(players[playerNum].hand)
        total = players[playerNum].numberTotal()
        print(players[playerNum].name, "has", total)
        if total > 21:
            print(players[playerNum].name, "has gone bust at", total)
            playing = False
                
        else:

            if playerNum == numberOfPlayers:
                if players[playerNum].numberTotal() < 17:
                    hit = "y"
                else:
                    hit = "n"
            else:
                hit = input("Would you like to hit or stand? ")

            if hit[0] in ["y","h"]:
                players[playerNum].dealCard(1)
            else:
                playing = False


for eachPlayer in players:
    if eachPlayer.numberTotal() > players[numberOfPlayers].numberTotal():
        winners.append(eachPlayer.name)

if len(winners) >= 1:
    print(", ".join(winners), "beat the dealer!")
else:
    print("No one beat the dealer...")
#dealer's hands
