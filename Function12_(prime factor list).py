#wap to input list of integers and extract the prime numbers
import math
def isPrime(num):
    flag=True
    for i in range(2,int((math.sqrt(num))+1)):
        if num==2:
            flag=True
            break
        if num%i==0:
            flag=False
            break
    return flag
def prime_factors(num):
    factor=[]
    for i in range(2,num+1):
        if(num%i==0):
            factor.append(i)
    prime_factor=list(filter(lambda x: isPrime(x),factor))
    print(prime_factor)
num=int(input("enter a number: "))
prime_factors(num)