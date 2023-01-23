def getAns(lenn,ar):
    if lenn == 2:
        return 1
    res = 0
    i = 0
    #print(ar)
    while i<lenn-2:
        if ar[i] == "0" and ar[i+1]=="1":
            res = res + 1
        i = i + 1
    #print(res)
    if ar[lenn-2] == "0":
        res = res + 1
    
    if ar[0] == "1":
        res = res + 1
    
    return res

t = int(input())
for tcase in range(t):
    lenn = int(input())
    ar = input()
    print(getAns(lenn,ar))