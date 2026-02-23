l0=list() #empty list creation method 1
l1=[] #empty list creation method 2
l2=[1,4]
l1.append(3) #append - add element from behind
l1.append(l2) #l2 added as list element
l0.extend(l2) #each individual element of l2 added 
print(l1,l0)

l7=[2,4]*3 #replication operator
print(l7)

l1=['a','b','c']
print('c' not in l1) #in, not in membership operator 

l8=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(l8[::-1]) #slicing operation reverse - not really reverse only for show
print(l8[:-1])
l8.reverse() #actually list is reversed
print(l8)
print(l8.index("wednesday")) 
print(l8.pop()) #remove last element
print(l8)
del l8[0] #delete the given element
print(l8)

#traversing a list
l2=[1,2,3,4,5]
n=len(l2)
i=0
while i<n:
    print(l2[i])
    i+=1
print("\n")