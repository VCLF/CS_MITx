import math

def isIn(char, aStr):
    aStr.lower()
    l = len(aStr)
    print(aStr)
    if char == aStr[l//2]:
        return True
    elif l == 1 or l == 0:
        return False
    elif char < aStr[l//2]:
        return isIn(char,aStr[0:l//2])
    elif char > aStr[l//2]:
        return isIn(char,aStr[l//2:])

def polysum(n,s):
    return polyarea(n,s) + polyper(n,s)**2

def polyarea(n,s):
    return (0.25*n*s**2)/(math.tan(math.pi/n))

def polyper(n,s):
    return n*s

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if aDict.values() == []:
        return None
    else:
        amount = {}
        mem = '0'
        for i in aDict.keys():
            quant = str(len(aDict.get(i)))
            amount[quant] = amount.get(quant,'') + i
            if quant > mem:
                mem = quant
        return amount.get(mem)