import time

countDowntime = int(input("enter a countdown time "))

for i in range(0,countDowntime):
    countDowntime -= 1
    time.sleep(1)
    print((countDowntime),"seconds left")


print("time's up")