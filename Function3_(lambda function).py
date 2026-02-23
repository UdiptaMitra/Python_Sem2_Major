square= lambda x:x*x
add= lambda x,y:x+y
max_item=lambda x,y: x if x>y else y

print(square(5))
print(add(2,3))
print(max_item(6,75))

check=lambda x: "even" if x%2==0 else "odd"
print(check(4))

a1=[2,3,4,5]
res=[val**2 for val in a1] #list comprehension
print(res)
#nested loop in list comprehension allowed

#a lambda function inside a function one var input in main other in lambda and both add return
def operation(x):
    return lambda y: x+y
f=operation(10)
print(f(5))

l1=[10,20,40,50]
result=map(lambda x:x*2,l1) #no loop happens, iterator generated, map object formed, lazy evaluation - computation delayed until required
result=list(result)#iterator extracts each value and the work happens
print(result)

'''map() takes two arguments - a function, an iterable
It applies the function to each element of the iterable one by one
The result is a map object (iterator).
We usually convert it into a list or tuple to see the output.
jotokhon na converted totokhon work not happen'''

m=map(lambda x:x*2,l1)
print(next(m))
print(next(m))
print(next(m)) #next is a built in method associated to map
print(next(m))#one by one output dey in order
#print(next(m)) #extra hole error
l5=[1,2,3,4]

l2=[x*2 for x in l1] #eager evaluation - byte code generated, all computation done at once
l3=list(map(lambda x:x*2,l1)) #lazy evaltuation - no byte code generated, computation done when needed

l4=list(filter(lambda x:x%2==0,l5)) #filter function filters out shit

print(l2)
print(l3)
print(l4)

students=[('a',90),('b',45),('c',20)]
students.sort(key=lambda x:x[1])
print(students)

calc=lambda x,y:x+y
res=calc(2,3)
print(res) #single value return directly

calc=lambda x,y:(x+y,x*y)
res=calc(2,3)
print(res) #multiple value return in tuple
res_a,res_m=calc(5,6) #tuple unpacking works
print(res_a,res_m)

def square(x):
    return x**2
result=list(map(square,a1))
print(result)

def is_even(i):
    return i%2==0
n=[10,23,35,24,56,78,99]

l1=[x for x in n if is_even(x)]
print(l1)

l2=list(filter(is_even,n))
print(l2)
l3=[y for y in filter(is_even,n)]
print(l3)

#for map method function getting called multiple times, one object for each call -  multiple map objects
#for filter only once called - one filter object

l3=sum((map(square,filter(is_even,n))))#sum of square of even num
#ekhane kothao list() na dileo cholbe sum(list) or list(filter)
print(l3)

l4=sum(map(lambda x: x**2,filter(lambda x: x%2==0,n))) #same using lambda function 
print(l4)

evens=filter(lambda x:x%2==0,n)
squares=map(lambda x:x**2,evens)
result=sum(squares)
print(result)


