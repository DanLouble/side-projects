count = 0

primenumbers = []

numTester = int(input("enter a number for all the prime up to the number "))
#if not numTester // 2 == 0 and not numTester // 3 == 0 and not numTester // 5 == 0:

primes =[]

for count in range(2, numTester + 1):
    prime = True
    for eachPrime in primes:
        if count % eachPrime == 0:
            prime = False
            break
    if prime:
        print(count)
        primes.append(count)
        
        #print(numTester

    
#print(primenumbers)

