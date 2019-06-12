def gcd(a, b):
    gcd = 1
    
    if a % b == 0:
        return b
    
    for k in range(int(b / 2), 0, -1):
        if a % k == 0 and b % k == 0:
            gcd = k
            break  
    return gcd
a = int(input())
b = int(input())
print(gcd(a, b))
