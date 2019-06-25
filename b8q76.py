ld=int(input())
if(ld>0):
	for i in range(2,ld):
		if(ld%i==0):
			print("yes")
			break
	else:
		print("no")
else:
	print("yes")
