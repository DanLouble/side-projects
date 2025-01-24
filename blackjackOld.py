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
        

def dealCard(numberOfCards):
    dealtCards = []
    for i in range(numberOfCards):
        card = random.choice(cardDeck)
        dealtCards.append(card)
        cardDeck.remove(card)
    return dealtCards


#dealer = 0

def numberTotal(cardHand):
    localTotal = 0
    aces = 0
    for eachCard in cardHand:
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

myHand = dealCard(2)

playing = True

valid = False
while not valid:
    try:
        betAmount = int(input("bet amount: "))
    except ValueError:
        continue
    if betAmount> gamblingBalance:
        print("you have insufficient funds")
        continue
    elif betAmount <= 0:
        print("Bet must be positive")
    valid = True

gamblingBalance -= betAmount
balanceUpdater()

dealerHand = dealCard(1)

if numberTotal(myHand) == 21:
        print(myHand)
        print("Blackjack! you win", int(2.5 * betAmount),"chips")
        gamblingBalance += 2.5 * betAmount
        playing = False


while playing:
    
    print(myHand)
    total = numberTotal(myHand)
    print("you have", total)
    if total > 21:
        print("you've gone bust at", total)
        print("dealer had",numberTotal(dealerHand))
        playing = False
    
    elif numberTotal(myHand) > numberTotal(dealerHand) and numberTotal(dealerHand) >= 17:
        print("congrats you win", int(2 * betAmount), "chips")
        gamblingBalance += 2 * betAmount
        print("dealer had",numberTotal(dealerHand))
        playing = False
    
    else:
        dealerTotal = numberTotal(dealerHand)
        print("dealer has", dealerTotal)

        hit = input("Would you like to hit or stand? ")

        if hit[0] in ["y","h"]:
            myHand += dealCard(1)
        
            

        else:
            while dealerTotal < 17:
                dealerHand += dealCard(1)
                dealerTotal = numberTotal(dealerHand)
                if dealerTotal > 21:
                    print("dealer has gone bust you win")
                    gamblingBalance += int(2 * betAmount)
                    playing = False
                #print("dealer has", dealerTotal)
            if total < dealerTotal:
                print("unlucky hands, you have", total)
            elif dealerTotal == total:
                gamblingBalance += betAmount
                print("you break even")
            else:
                print("congrats you win", int(2 * betAmount), "chips")
                gamblingBalance += 2 * betAmount
                print("dealer had",dealerTotal)
            playing = False
    

#dealer's hands

        
    

