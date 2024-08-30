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
        self.autowin = None
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
    
    def printHand(self):
        for eachCard in self.hand:
            print(*eachCard, sep=" of ", end="")
            if self.hand.index(eachCard) != len(self.hand) - 1:
                print(", ", end="")
        print()

    def setAutowin(self, autowinValue):
        self.autowin = autowinValue


players = []
numberOfPlayers = int(input("How many players? "))
for i in range(numberOfPlayers):
    name = input("What is your name? ")
    players.append(Player(name))
players.append(Player("DEALER"))

winners = []

for playerNum in range(numberOfPlayers + 1):

    playing = True

    if players[playerNum].numberTotal() == 21:
        players[playerNum].printHand()
        print("Blackjack!")
        players[playerNum].setAutowin(False)
        playing = False

    players[playerNum].dealCard(2)

    
    print("\n" + players[playerNum].name + "'s Turn")
    while playing:
        
        players[playerNum].printHand()
        total = players[playerNum].numberTotal()
        if total > 21:
            playing = False
            players[playerNum].setAutowin(False)
            print(players[playerNum].name, "has gone bust at", total)

        elif len(players[playerNum].hand) == 7:
            print("7 Card Charlie")
            players[playerNum].setAutowin(True)
            playing = False

        else:
            print(players[playerNum].name, "has", total)

            #Dealer making decision
            if playerNum == numberOfPlayers:
                if players[playerNum].numberTotal() < 17:
                    hit = "y"
                    print("Dealer hits...")
                    time.sleep(1)
                else:
                    hit = "n"
                    print("Dealer stands.")
                    time.sleep(1)
            else:
                hit = input("Would you like to hit or stand? ")

            if hit[0] in ["y","h"]:
                players[playerNum].dealCard(1)
            else:
                playing = False


for eachPlayer in players:
    if (eachPlayer.numberTotal() > players[-1].numberTotal() and eachPlayer.autowin != False) or eachPlayer.autowin == True:
        winners.append(eachPlayer.name)

if len(winners) > 1:
    print(", ".join(winners[:-1]), "and", winners[-1], "beat the dealer!")
elif len(winners) == 1:
    print(winners[0], "beat the dealer!")
else:
    print("No one beat the dealer...")
#dealer's hands
