ld1,ld2=map(int,input().split())
list=[int(i) for i in input().split()]
count = 0

for i in list:
	if i == ld2:
		count = 1
if count == 1:
	print("yes")
else:
	print("no")
