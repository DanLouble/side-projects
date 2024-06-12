import time

upperLimit = 10.2
lowerLimit = 9.8

print("Get between", lowerLimit, "and", upperLimit, "to win")

input("press enter to play ")
start = time.time()
input("Press enter on 10 seconds ")

end = time.time()

time = round(end-start,2)

print(time,"seconds")

if lowerLimit <= time < upperLimit:
    print(time,"congratulations you win")

else:
    print("unlucky, you were",round(abs(10 - time),2),"seconds off")