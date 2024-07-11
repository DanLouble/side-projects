import numpy

count = 0

primenumbers = []

numTester = int(input("enter a number for all the prime up to the number "))
#if not numTester // 2 == 0 and not numTester // 3 == 0 and not numTester // 5 == 0:
    

while count <= numTester:
    #if count == 2:
        #print(count)
    if not count % 2 == 0 and not count % 3 == 0 and not count % 5 == 0:
        print(count)
        primenumbers.append(count)
        
        #print(numTester

    count+=1
#print(primenumbers)