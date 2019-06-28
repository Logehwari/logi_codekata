ld,lg=map(str,input().split())
if(len(ld)!=len(ld)):
  print("no")
c1=[ld.count(i) for i in ld]
c2=[lg.count(i) for i in lg]
if c1==c2:
  print("yes")
else:
  print("no")
