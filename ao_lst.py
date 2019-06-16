def Average(lst): 
    return sum(lst) / len(lst) 
num = int(input())
lst = list(map(int,input().split())) 
average = Average(lst) 
print(int(average)) 
