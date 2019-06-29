l1,l2=map(str,input().split())
if len(l1)==len(l2):
  for i in range(0,len(l1)):
    if l1[i]==l2[i]:
      print("yes")
      break
  else:
      print("no")
