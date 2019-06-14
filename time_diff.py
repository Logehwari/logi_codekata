
hr1, min1 = [int(x) for x in input().split()]
hr2, min2 = [int(y) for y in input().split()]
hrn = abs(hr1 - hr2)
minn = abs(min1 - min2)
print(hrn,minn)
