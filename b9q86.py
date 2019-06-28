ld=list(input())
lg=[]
for i in ld:
    if i not in lg:
        lg.append(i)
if ld==lg:
    print("Yes")
else:
    print("No")
