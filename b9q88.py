ld,lg=map(int,input().split())
x1=ld
y1=lg
while(lg):
    ld,lg=lg,ld%lg
z1=(x1*y1)//ld
print(z1)
