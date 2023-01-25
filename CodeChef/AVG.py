def calcAns(N,K,V,arr):
    summNeeded = V*(N + K)
    summ = sum(arr)
    
    dif = summNeeded - summ
    if dif > 0 and dif%k ==0:
        return dif//k
        
    return -1

t = int(input())

while t>0:
    n,k,v=map(int,input().split())
    avgr=list(map(int,input().split()))
    #print(avgr)
    print(calcAns(n, k, v,avgr))
    t-=1