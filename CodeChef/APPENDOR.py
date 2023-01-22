t = int(input())

for i in range(t):
    a,b = list(map(int,input().split(" ")))
    arr = list(map(int,input().split(" ")))
    res = 0
    for t in arr:
        res |= t
    ans = res ^ b
    if ans|res != b:
        print(-1)
        continue
    print(res ^ b)