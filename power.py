def power(num,exp):
    if(exp==1):
        return(num)
    if(exp!=1):
        return(num*power(num,exp-1))
num=int(input())
exp=int(input())
print(power(num,exp))
