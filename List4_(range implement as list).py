#even numbers from 2 to 10 print
i=0   
v2=list(range(2,11,2)) #using range in while
while i<len(v2):
    print(v2[i])
    i=i+1
print("\n")   

#range behaviour as function
v1=list(range(2,10,3))
print(v1)
print("\n")   
#range type cast as list gives sequence of numbers
#not mandatory to use range in for loop