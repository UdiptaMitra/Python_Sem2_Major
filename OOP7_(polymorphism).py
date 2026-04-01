class Calculator:
    def multiply(self,a=1,b=1,*args):
        result=a*b
        for num in args:
            result*=num
        return result
    
#create object
calc=Calculator()

#using default argument
print(calc.multiply())
print(calc.multiply(4))

#using multiple argument
print(calc.multiply(2,3))
print(calc.multiply(2,3,4))

#handling polymorphism with class
class Circle:
    def area(self):
        print("Area = pi X r X r")
class Square:
    def area(self):
        print("Area= l X l")
def showarea(shape):
        shape.area()

c=Circle()
s=Square()
showarea(c)
showarea(s)

#operator overloading
class Number:
    def __init__(self,value):
          self.value=value
          #overloading + operator
    def __add__(self,other):
         return Number(self.value + other.value)
    def __str__(self): # eta na dile map object dekhache
         return str(self.value)
n1=Number(10)
n2=Number(20)
n3=Number(10)
result=n1+n2+n3
print(result)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
         if self.marks>other.marks:
              return Student(self.name,self.marks)
         else:
              return Student(other.name,other.marks)
    def __str__(self): # eta na dile map object dekhache
         return str(self.name)
stud1=Student("Udipta",100)
stud2=Student("Bindi",80)
res=stud1>stud2
print(res)

class Vector:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return Vector((self.x[0]+other.x[0],
                       self.x[1]+other.x[1]))
    def __str__(self): # eta na dile map object dekhache
         return str(self.x)
stud1=Vector((1,2))
stud2=Vector((3,6))
res=stud1+stud2
print(res)

class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    def __add__(self,other):
         n=len(other.matrix)
         m=len(other.matrix[0])
         matr3=[]
         for rows in range(n):
              rowsum=[]
              for cols in range(m):
                   rowsum.append(self.matrix[rows][cols]+other.matrix[rows][cols])
              matr3.append(rowsum)
         return matr3
    def __sub__(self,other):
         n=len(other.matrix)
         m=len(other.matrix[0])
         matr3=[]
         for rows in range(n):
              rowsum=[]
              for cols in range(m):
                   rowsum.append(self.matrix[rows][cols]-other.matrix[rows][cols])
              matr3.append(rowsum)
         return matr3


matr1=Matrix([[1,2],[3,4],[5,6]])
matr2=Matrix([[0,9],[2,7],[5,6]])
res=matr1+matr2
print(res)
res=matr1-matr2
print(res)

