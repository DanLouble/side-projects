import numpy


def binarysearch(array, low, high, x):

    if high >= low:
        mid = (high + low) // 2

        if array[mid] == x:
            return mid
        
        elif array[mid] > x:
            return binarysearch(array, low, mid - 1, x)

        else:
            return binarysearch(array, mid + 1, high, x)

    else:
        return -1


randomNumber = numpy.random.randint(1,100, size= 101)

array = randomNumber
    
#valueNum = int(input("how many values do you have? "))

x = int(input("enter the number to search for: "))

#for i in range(0,valueNum):
    #value = int(input("enter value: "))
    #array.append(value)

array.sort()

result = binarysearch(array, 0, len(array)-1, x)



if result != -1:
    print("your number is present at index", str(result)+" (value", str(result+1) +")")
    print(array)
else:
    print("your number is not present in array")
    