ld,lg=map(int,input().split())
cnt=0
for i in range(ld,lg+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
                
        else:
            cnt=cnt+1
print(cnt)
