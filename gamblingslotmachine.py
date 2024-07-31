import random

#gamblingBalance = 0

spin = input("enter 'Play' to play: ")
spin.lower


icons = ["Jacks","Queens","Kings","Jesters","Gold"]
#win = False

try:

    while spin == "play" or spin[0] == "y":
        

        col1 = random.choice(icons)
        col2 = random.choice(icons)
        col3 = random.choice(icons)

        #for eachcolumn in [col1,col2,col3]:
        
        print(" \n"+ col1,",",col2,",",col3)
        if col1 == col2 and col2 == col3:

            print("Jackpot! you win 100 chips")
            #gamblingBalance += 100
        elif col1 == col2 or col2 == col3 or col1 == col3:
            print("so close:( keep chasing the dragon")
        else:
            print("you suck")
        
        
        spin = input("keep playing? ")
except IndexError:
    pass
    
