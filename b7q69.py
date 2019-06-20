ld1,ld2=map(int,input().split())
ld = ld1-ld2
if ld % 2 == 0:
	print("even")
else:
	print("odd")
