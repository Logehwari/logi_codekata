ld=input()
for i in ld:
  if(i=='/'):
    lg=ld.split('/')
    print(int(int(lg[0])/int(lg[1])))
  elif i=='%':
    lg=ld.split('%')
    print(int(int(lg[0])%int(lg[1])))
