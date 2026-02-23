#decorator concept - basically function get called as parameter but without crowding the program

def deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@deco #@<decorator name> - takes greet method as function
def greet():
    print("hi guys")
    return

@deco
def ABCD():
    print("convergence incoming!!")
    return

print(greet())
print(ABCD())