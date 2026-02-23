import sys

b=5.99 #float
c=True #boolean
var1=6.5
var2=float(6.5) #type casting explicit
complex1=0+0j #complex=a+bj
complex2=3+4j
print(complex1+complex2)
print(complex1*complex2)
print(sys.getsizeof(complex1))
print(sys.getsizeof(var2)) 
#int-28, float-24, char-42, bool-28, complex-32 (minimum sizes)

list1=[2,3,6]
print(list1)
list1[0]=5
print(list1) #list is mutable
list2=[1,'a',"abc",0.99,True,[0,4,3]] #list can contain elements with diff datatype unlike arrays
print(list2)

set1={1,2,3} #set is ordered, no duplicate elemts allowed, mutable
frozenset1=frozenset([1,2,3]) # same as set, immutable
print(set1,frozenset1)

print("""all day is
fun day""")#print in diff line method 1
print("all day \n is fun day") #print in diff line method 2

#conditional statement
a=15 
b=10
if a==15:
    print("the num is 15")
else:
    print("the num is not 15")   