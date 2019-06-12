N = int(input())
K = int(input())

array=list(map(int,input().split()))
temp = 0
for j in range(K):
	temp  = temp + array[j]
print(temp)
