l1=int(input())
l2=0
while(l1>0):
  l3=l1%10
  l2=l2*10+l3
  l1=l1//10
print(l2)
