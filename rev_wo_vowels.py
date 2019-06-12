def reverse(str): 
    str = str[::-1] 
    return str 
str = input()
newstr = str;
vowels = ('a', 'e', 'i', 'o', 'u');
for x in str.lower():
    if x in vowels:
    	newstr = newstr.replace(x,"");
print(reverse(newstr));
