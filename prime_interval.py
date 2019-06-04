l1 = int(input())  
l2 = int(input()) 
  
for i in range(l1,l2 + 1):  
   if i > 1:  
       for j in range(2,i):  
           if (i % j) == 0:  
               break  
       else:  
           print(i)  
