def smallest(arr,n): 
  
   
    min = arr[0] 
    for i in range(1, n): 
        if arr[i] < min: 
            min = arr[i] 
    return min
  
n = 10
arr = list(map(int,input().split()))
Ans = smallest(arr,n) 
print (Ans) 
