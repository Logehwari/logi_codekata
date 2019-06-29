lg=input()
l=[lg[i] for i in range(len(lg)) if i%2==0]
l1=[lg[i] for i in range(len(lg)) if i%2!=0]
for j in range(len(lg)//2):
  print(l1[j]+l[j],end="")
