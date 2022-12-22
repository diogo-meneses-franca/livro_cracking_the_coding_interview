import math
def isPermutation(firstWord, secondWord):00
    first = firstWord
    second = secondWord
    sizeA = len(first)
    sizeB = len(second)
    menor = ""
    maior = ""
    mini = []
    maxi = []
    if( sizeA < sizeB):
        menor = first
        maior = second
    elif(sizeB < sizeA):
        menor = second
        maior = first
    for i in range(0, len(menor)):
        mini.append(menor[i])
    for j in range(0, len(maior)):
        maxi.append(maior[i])
    print(mini)
    print(maxi)

isPermutation("perucada", "pitoco")


    
    
