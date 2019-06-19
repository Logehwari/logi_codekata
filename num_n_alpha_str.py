str1=input()
alpha=False
numbr=False
for i in str1:
  if(i.isalpha()==True):
    alpha=True
  if(i.isdigit()==True):
    numbr=True
if(alpha==True and numbr==True):
  print("Yes")
else:
  print("No")
