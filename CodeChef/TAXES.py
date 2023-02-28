# cook your dish here
t = int(input())
for ti in range(t):
    x = int(input())
    if x > 100:
        print(x-10)
        continue
    print(x)