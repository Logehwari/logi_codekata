l1,l2=map(int,input().split())
i = 1
while(i <= l1 and i <= l2):
    if(l1 % i == 0 and l2 % i == 0):
        gcd = i
    i = i + 1
print(gcd)
