class BankAccount:
    
    def __init__(self): # init is initialiser similar to constructor. 
        # initialises objects of a class
        # whenever we call constructor we get the current condition of an object. 
        # constructor called, new instance created. 
        # alada kore object toirir somoy constructor call korina
        #self is mandatory parameter of constructor
        self.name=input("enter the name of account holder")
        self.balance=int(input("enter the balance"))

#name balance - constructor variable 
b1=BankAccount() 
print(b1.name)
print(b1.balance)
#dubar korle different instances and different values
b2=BankAccount()
print(b2.name)
print(b2.balance)
#b1,b2 - objects


