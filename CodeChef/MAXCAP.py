T = int(input())
for tes in range(T):
    X, Y = map(int,input().split(" "))
    if X <= 8  and X * Y <= 500:
        print("YES")
    else:
        print("NO")