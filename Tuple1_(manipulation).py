t=(10,20,30) #tuple -  immutable
#memory efficient compared to list
#tuple can hold heterogenous type of data
import sys
print(sys.getsizeof(t)) #- 64
print(sys.getsizeof(list(t))) #- 88

#traversing a tuple:
for i in t:
    print(i)

#concatenation operation
t2=(40,50)
t3=t+t2
print(t3)

#replication operation
print(t2*4)

#methods for both list and tuple
print(len(t)) #length of tuple
print(min(t)) #max value
print(max(t)) #min value
print(sum(t)) #sum of value
print(t.index(20)) #position of given element

#method for only tuple
print(t.count(30)) #an argument whose freq to be found
