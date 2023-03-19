pow3s = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721]
def getAns(n):
    #print(len(pow3s))
    k = 0
    while k < 17 and pow3s[k] <= n:
        k+=1
    
    #n < 10^8 so total possible possibilities are 2**17.
    total_possibilities = 2**k - 1
    overall_min_1s = 100
    for pos in range(total_possibilities):

        current_1s = 0
        #this variable will represent how much binary contribution needed, 
        # as remaining contri  is coming from 3s
        binary_input_needed = n
        for j in range(17):
            if pos&(1<<j):
                binary_input_needed-=pow3s[j]
                current_1s+=1
                if binary_input_needed < 0:
                    break
        
        #print("binary_input_needed_was"+str(binary_input_needed)+"and cur 1s"+str(current_1s))
        if binary_input_needed >= 0:
            current_1s+=str(bin(binary_input_needed)).count('1')
            overall_min_1s = min(overall_min_1s,current_1s)
            #print("now"+str(overall_min_1s))
    
    return overall_min_1s

t = int(input())
for _ in range(t):
    n = int(input())
    print(getAns(n))