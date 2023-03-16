T = int(input())
for tes in range(T):
    bookn = int(input())
    pageAr = list(map(int,input().split(" ")))
    if len(pageAr) == 1:
        print("NO")
        continue
    
    odcnt = 0
    for x in pageAr:
        if x%2 == 1:
            odcnt = 1 - odcnt
    
    if odcnt == 0:
        print("YES")
    else:
        print("NO")