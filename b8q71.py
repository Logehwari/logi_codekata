num=input()
ld=""
for i in num:
  ld=i+ld
  if(num==ld):
    print("yes")
    break
else:
    print("no")
