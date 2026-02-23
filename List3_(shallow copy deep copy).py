import copy

#no copy created, l1 and l3 are referring to same memory location all changes shown up
l1=[9,[7,8]]
l3=l1
l1[0]=0
l1[1][0]=1
print(l1,l3)

l4=[0,[1,2],[3,4]] #initial list
l5=l4.copy() #shallow copy
l6=copy.deepcopy(l4)#deep copy
l4[1][0]=2 #change in inner list element
l4[0]=9 #change in outer list element
print(l4,l5,l6)

'''shallow copy creates new list but not copies of nested objects 
(outer not change but inner list element change)
deep copy creates new list and new copies of all nested objects
(outer inner no element change whole list intact)'''