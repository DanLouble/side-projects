import random


def balanceUpdater():

    
    with open("/home/danny/Desktop/vs code/balance.txt","w")as balanceFile:
        balanceFile.write(str(gamblingBalance))



with open("/home/danny/Desktop/vs code/balance.txt", "r") as balanceFile:
    gamblingBalance = int(balanceFile.read())
    if gamblingBalance <= 20:
        gamblingBalance += 100
    

spin = input("enter 'Play' to play: ")
spin.lower


icons = ["Jacks","Queens","Kings","Jesters","Gold"]

iconsDict = {
    "Jacks": 2,
    "Queens": 5,
    "Kings": 10,
    "Jesters": 1,
    "Gold": 20
    }
#win = False

try:

    while spin == "p" or spin[0] == "y":
        
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


        
        columns = []
        for i in range(3):
            columns.append(random.choice(icons))

        #for eachcolumn in [col1,col2,col3]:
        print("")
        print(*columns)
        if all(eachColumn == columns[0] for eachColumn in columns):
            gamblingBalance += betAmount * iconsDict[columns[0]]
            balanceUpdater()
            print("Jackpot! you win", betAmount * iconsDict[columns[0]], "chips")
            #gamblingBalance += 100
        elif columns[0] == columns[1] or columns[1] == columns[2] or columns[0] == columns[2]:
            print("so close:( keep chasing the dragon")
            gamblingBalance += betAmount*0.5
        else:
            print("you suck")
        gamblingBalance = int(gamblingBalance)
        print("gambling balance:", gamblingBalance)
        
        
        if gamblingBalance > 0:
            spin = input("keep playing? ")
        else: 
            print("error, insuficient funds to gamble")
            quit()
except IndexError:
    pass
    
