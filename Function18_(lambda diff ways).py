'''way 1'''
#lambda can be combined with list comprehension
func=[lambda arg=x:arg*10 for x in range(1,5)]
for i in func:
    print(i()) #i is a lambda function no manual argument

'''way 2'''
f1=lambda x: x*10 
for x in range(1,5):
    a=f1(x)
    print(a)

'''way 3'''
l1=[i for i in range(1,5)]
l2=[f1(i) for i in l1]
print(l2)

'''way 4'''
list1=map(lambda x: x*10,list(range(1,5)))
print(list(list1))



