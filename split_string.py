# your code goes here
def split(word): 
    return [char for char in word]  
      
# Driver code 
word = 'geeks'
st1 = split(word)
n = len(str1)
odd_li = []
even_li = []
for i in range(n):
	if i%2 != 0:
		odd_li.append(st1[i])
	else:
		even_li.append(st1[i])
		
print(even_li)
print(odd_li)
