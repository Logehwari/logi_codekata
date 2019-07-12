n=int(input())
if n<=0:
	print("invalid input")
while(n<=0):
	print("enter valid input: ")
	n=int(input())
for i in range(n):
	print('  '*(n-i-1)+'* '*(i+1)+'* '*i)
for i in range(n-1):
	print('  '*(i+1)+'* '*(n-i-1)+'* '*(n-i-2))
