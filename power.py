def power(num,expo):
    if(expo==1):
        return(num)
    if(expo!=1):
        return(num*power(num,expo-1))
num=int(input())
expo=int(input())
print(power(num,expo))
