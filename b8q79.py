ld1,ld2=list(map(int,input().split()))
p=ld1*ld2
for x in range(0,p+1):
  if(x**2==p):
    print("yes")
    break;
else:
  print("no")
