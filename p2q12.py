n,m=map(int,input().split())
ld=list(map(int,input().split()))
for i in range(0,m):
    ld=[ld[-1]]+ld[:-1]
print(*ld,end=' ')
