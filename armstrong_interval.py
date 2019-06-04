l1 = int(input())  
l2 = int(input()) 
  
for n in range(l1,l2 + 1):
	sum = 0
	temp = n
	while temp > 0:
		digit = temp % 10
		sum += digit ** 3
		temp //= 10
	if n == sum:
		print(n)
