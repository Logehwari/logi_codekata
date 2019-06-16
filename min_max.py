
def smallest(arr,n): 
  
   
    min = arr[0] 
    for i in range(1, n): 
        if arr[i] < min: 
            min = arr[i] 
    return min
  
def largest(arr,n): 
  
   
    max = arr[0] 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
  
n = int(input())
arr = list(map(int,input().split()))
Ans = largest(arr,n) 
Ans1 = smallest(arr,n)
print (Ans1,Ans)
  
