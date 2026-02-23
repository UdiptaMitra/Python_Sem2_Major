#kwargs not working
'''import math
def deco(func):
    flag=0
    def wrapper(*args,**kwargs):
        print(kwargs)
        if len(kwargs.values())>0:
            for v in kwargs.values():
                if v>0:
                    flag=1
                    continue
                else:
                    print("theres a negative number")
                    break
        if flag==1:
            print("correct")

        print(func(*args,**kwargs))
    return wrapper

@deco
def greet():
    return "hello"
greet()

@deco
def square(a):
    return a*a
square(2)

@deco
def logarithm(a,b):
    return math.log(a,b)
logarithm(2,10)

@deco
def summation(a,b,c):
    return a+b+c
summation(1,2,3)
'''
#without kwargs working
import math

def deco(func):
    def wrapper(*args):
        flag=0
        if len(args)==0:
            flag=1
        for i in args:
            if i>=0:
                flag=1
                continue
            else:
                break
        if flag==1:
            return func(*args)
        else:
            return "oops a negative number"
    return wrapper

@deco
def greet():
    return 'hello'
print(greet())

@deco
def square(a):
    return a*a
print(square(-4))

@deco
def logarithm(a,b):
    return math.log(a,b)
print(logarithm(2,10))

@deco
def summation(a,b,c):
    return a+b+c
print(summation(9,2,3))

