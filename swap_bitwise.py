a, b = [int(x) for x in input().split()]
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)
