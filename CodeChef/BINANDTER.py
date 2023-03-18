def giveRem(num):
    b = [1,2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728]
    a = [1,3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163]

    ai = 0
    bj = 0

    while a[ai+1] <= p:
        ai +=1

    rema = p - a[ai]
    if rema == 0:
        return ai,0
    
    while b[bj+1] <= p:
        bj +=1
    
    remb = p - b[bj]

    if remb == 0:
        return bj,0
    
    if rema < remb:
        return ai,rema
    else:
        return bj,remb

T = int(input())
for tes in range(T):
    p = int(input())
    sumi = 0
    while True:
        k,rem = giveRem(p)
        print((k,rem))
        sumi+=1
        p = rem
        if p == 0:
            break
    print(sumi)