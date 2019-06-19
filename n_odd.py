n,k=map(int,input().split())
inlst=list(map(int,input().split()))
lst=[]
for i in inlst:
  if(i%2!=0):
    lst.append(i)
print(lst[k-1])
