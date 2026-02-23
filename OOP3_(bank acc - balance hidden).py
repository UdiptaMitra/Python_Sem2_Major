class BankAccount:
    def __init__(self,n,b):
        self.name=n
        self.__balance=b
    def view_balance(self):
        return self.__balance

n=input("enter the name of account holder")
b=int(input("enter the balance"))
b1=BankAccount(n,b)
print(b1.name)
print(b1.view_balance())
#print(b1.balance)#error shown because balance is hidden __balance






