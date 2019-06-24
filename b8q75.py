
str1=input()
l1=int(len(str1)/2)
if(len(str1)%2!=0):
    c=str1[:l1]
    b=str1[l1+1:len(str1)]
    str2=c+"*"+b
    print(str2)
elif(len(str1)%2==0):
    c=str1[:l1-1]
    b=str1[l1+1:len(str1)]
    str4=c+"**"+b
    print(str4)
