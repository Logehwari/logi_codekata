def largest(arr,n): 
  
   
    min = arr[0] 
    for i in range(1, n): 
        if arr[i] < min: 
            min = arr[i] 
    return min
  
n = int(input())
arr = list(map(int,input().split()))
Ans = largest(arr,n) 
print (Ans) 
  
