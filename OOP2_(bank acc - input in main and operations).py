class BankAccount:
    interest_rate=0.5 #class variable 
    def __init__(self,n,b):
        self.name=n
        self.balance=b
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return self.balance
        return "invalid deposit amount"
    def withdraw(self,amount):
        if amount>0 & amount<=self.balance:
            self.balance-=amount
            return self.balance
        return "invalid withdrawal amount or insufficient balance"
    def apply_interest(self):
        interest_amt=self.balance*BankAccount.interest_rate #class var class er nam niye dakte hbe
        self.balance+=interest_amt 

n=input("enter the name of account holder")
b=int(input("enter the balance"))
b1=BankAccount(n,b)
print(b1.name)
print(b1.balance)
#different instance but same value
b3=BankAccount(n,b)

b2=BankAccount("Udipta",2000)
print(b2.name)
#print(b2.balance)
#print(b1.deposit(-1)) - error message shown
print(b1.deposit(1000)) #self-b2 thats why no extra parameter
print(b2.withdraw(500))
print("b1 bank balance deposit 1000 "+str(b1.balance))
print("b2 bank balance withdraw 500 from 2000 "+str(b2.balance))
b2.apply_interest()
print("b2 balance after interest increase "+str(b2.balance))