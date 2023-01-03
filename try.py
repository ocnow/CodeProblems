print(3881//1000)

def getRoman(num : int) -> str:
    a = num//1000
    b = num%1000
    
    c = b//500
    d = b%500

    e = d//100
    f = d%100

    g = f//50
    h = f%50

    i = h//10
    j = h%10

    k = j//5
    l = j%5

    m = l

    return (a*'M') + (c* 'D') + (e * 'C') + (g * 'L') + (i * 'X') + (k * 'V') + (m * 'I')

print(getRoman(51))
