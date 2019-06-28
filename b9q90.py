ld=input()
lg=[]
for i in ld:
  if i.isnumeric():
    lg.append(i)
print("".join(lg))
