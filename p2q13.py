ld=int(input())
lg=0
while(ld>0):
    p=ld%10
    ld=int(ld/10)
    lg+=p*p
print(lg)   
