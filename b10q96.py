l,m,n=map(int,input().split())
ld=0
for i in range(1,n+1):
  ld+=l+m*(n-i)
print(ld)
