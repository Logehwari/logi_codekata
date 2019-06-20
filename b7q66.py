ld = int(input())
  

if ld > 1: 
      
  
   for i in range(2, ld//2): 
         
      
       if (ld % i) == 0: 
           print("no") 
           break
   else: 
       print("yes") 
  
else: 
   print("no") 
