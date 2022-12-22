import math
a = "mussum"

def isPalindrome(a):
    pal = 0
    n = 0
    if ((len(a) % 2) == 0):
        n = int(len(a)/2)
    else:
        n = len(a)
    for i in range(0, n):
        if(a[i] == a[-i-1]):
            pal += 1
    if(pal == n):
        return True
    else:
        return False

res = isPalindrome(a)
print(res)