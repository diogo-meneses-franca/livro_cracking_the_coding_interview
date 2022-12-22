def checkIfInsertedChar(oldStr, newStr):
    szOld = len(oldStr)
    szNew = len(newStr)
    if(szNew != szOld +1):
        return False
    newSorted = sorted(newStr)
    eq = 0
    for i in range(0, szOld):
        if(binarySearch(oldStr[i], newSorted, 0, szNew - 1) != False):
            eq += 1
    if(eq == szNew - 1):
        return True
    else:
        return False

def checkIfRemovedChar(oldStr, newStr):
    szOld = len(oldStr)
    szNew = len(newStr)
    sortedOld = sorted(oldStr)
    eq = 0
    for i in range(0, szNew):
        isInside = (binarySearch(newStr[i], sortedOld, 0, szOld -1))
        if(isInside == True):
            eq += 1
    if(eq == szNew and szNew == szOld -1):
        return True
    else:
        return False

def checkIfReplacedChar(oldStr, newStr):
    if(len(oldStr) != len(newStr)):
        return False
    sortedNew = sorted(newStr)
    dif = 0
    eq = 0
    for i in range(0, len(sortedNew)):
        if(binarySearch(oldStr[i], sortedNew, 0, len(sortedNew) - 1) == False):
            dif += 1
        else:
            eq += 1
    if(dif == 1 and eq == len(newStr) - 1):
        return True
    else:
        return False

def binarySearch(charac, word, start, end):
    if(end >= start):
        mid = (end + start) // 2
        if(charac == word[mid]):
            return True
        elif(charac > word[mid]):
            return binarySearch(charac, word, mid + 1, end)
        else:
            return binarySearch(charac, word, start, mid - 1)
    else:
        return False

def checkEdits(oldStr, newStr):
    ins = checkIfInsertedChar(oldStr, newStr)
    rem = checkIfRemovedChar(oldStr, newStr)
    rep = checkIfReplacedChar(oldStr, newStr)
    if(ins == True or rem == True or rep == True):
        return True
    else:
        return False


"""
res = checkIfRemovedChar(b, a)
print(res)"""

a = "ple"
b = "pled"
res = checkEdits(a,b)
print(res)

    