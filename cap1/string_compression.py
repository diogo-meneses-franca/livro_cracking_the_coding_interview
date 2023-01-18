def stringCompression(string):
    counter = 0
    newstring = []
    for i in range(0,len(string)-1):
        counter += 1
        if(string[i] != string[i + 1] or i + 1 >= len(string)-1):
            newstring.append(string[i])
            newstring.append(counter)
            counter = 0
    if(len(newstring) < len(string)):
        return newstring
    else:
        return string

word = "aacdbbbbwww"
test = stringCompression(word)
print(test)