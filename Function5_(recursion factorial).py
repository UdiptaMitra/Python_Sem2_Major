'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a number: "))
print("the factorial is ",factorial(n))'''

def factorial(n,depth=0):
    indent= " " *depth
    print(f"{indent}Call factorial({n})")
    if n==0:
        print(f"{indent}Return 1")
        return 1
    else:
        result=n*factorial(n-1,depth+1)
    print(f"{indent}Return {result}")
    return result              
n=int(input("enter a number: "))
print("the factorial is ",factorial(n))