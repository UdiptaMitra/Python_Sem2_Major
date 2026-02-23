#we can use method and function interchangeably
def greet(t):
    print("hello "+t)

def greet_again(v1):
    def get_message(): #function definition inside funcion not recursion
        return "hello "
    s1=get_message()+v1
    print(s1)

    
name=input("enter the name: ")
greet(name)
greet_again(name)

#number of argument fixed in below functions
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b #return one value

#python is called first class method as function can be passed as an argument
def operate(func,x,y): #even a function can become a parameter
    return(func(x,y))
print(operate(add,4,5))
print(operate(multiply,4,5))

def calculation(a,b=6): #default para,meter can be overwritten if parameter passed
    return a+b,a-b,a*b #return multiple value value
x,y,z=calculation(2,3) #explicit definition where sequence of values matter
#seqn of passed parameter is same of seqn of formal parameter in function definition
print(x,y,z)
x,y,z=calculation(b=3,a=2) #keyword definition where sequence of values not matter as var name mentioned
print(x,y,z)


#number of output not fixed in *, **
def add(*n): #* n is tuple type of data
    sum=0
    for i in n:
        sum+=i
    print(type(n))
    print(sum)
add(2,3,4,5)

def student(**details): #** dictionary type of data
    for k,v in details.items():
        print(k,":", v)
    print(type(details))
student(name="student",roll="730")


def funct(*args): #tuple
    return sum(args)
print(funct(1,2,3)) #only take argument not their names

def funct1(**kwargs): #dict
    for k,val in kwargs.items():
        print(k,val)
funct1(a=1,b=2,c=3) #any number of arguments
funct1(a=1,b=2)