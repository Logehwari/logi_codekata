ld=int(input())
prod=1
while(ld>0):
  x=ld%10
  ld=ld//10
  prod*=x
print(prod)
