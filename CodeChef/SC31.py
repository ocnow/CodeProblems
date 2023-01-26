t = int(input())
while t > 0:
    N = int(input())
    ans = 0
    for ni in range(N):
        c = int(input(),2)
        ans = ans ^ c
    bins = "{0:b}".format(ans)
    finalans = 0
    for x in bins:
        if x == '1':
            finalans += 1
    print(finalans)
    t -=1