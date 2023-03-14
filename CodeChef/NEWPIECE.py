Tes = int(input())
for t in range(Tes):
    a,b,x,y = map(int,input().split(" "))
    if a == x and b == y:
        print(0)
    elif (a+b) %2 != (x+y)%2:
        print(1)
    else:
        print(2)