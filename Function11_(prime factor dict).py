#prime factorisation dictionary key-factors, value-number of times repeated
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
    count_prime=[]
    for i in range(2,num+1):
        if(num%i==0):
            factor.append(i)
    prime_factor=list(filter(lambda x: isPrime(x),factor))

    for i in range(len(prime_factor)):
        count=0
        while(num%prime_factor[i]==0):
            count+=1
            num=num/prime_factor[i]
        count_prime.append(count)
    print(dict(zip(prime_factor,count_prime)))
num=int(input("enter a number: "))
prime_factors(num)

