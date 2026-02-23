#wap to create user defined function to check whether a number is prime or not
import math
def prime(num):
    flag=0
    for i in range(2,int((math.sqrt(num))+1)):
        if num==2:
            flag=0
            break
        if num%i==0:
            flag=1
            break
    return flag
num=int(input("enter a number: "))
if prime(num)==1:
    print("the number is composite")
else:
    print("the number is prime")
