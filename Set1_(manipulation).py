set1={} #NOT empty set its empty DICTIONARY
set0=set() #empty set
set2={1,2,3}
print(set2)
list1=[1,2,2,3,3,4,5,4,5,6,7]
print(set(list1)) #list typecasted to set rep elem removed

for i in set2:
    print(i) #cant traverse by index coz set unordered

#egulo sob set e kaj korbe not in frozenset
set2.add(10) #add 1 elem
set2.update([5,65,7]) #add a list of elem as indiv elem not as list - 
print(set2)
set2.remove(65) #removes the given elem but shows error if thats not present
set2.discard(13) #safest - removes the given elem not show error if thats not present
set2.pop() # removes a random elem as not ordered
print(set2)
set2.clear()
print(set2) #return empty set

#set operation method for both set and frozenset
s1={1,2,3,4}
s2={2,4,6,8}
print(s1|s2)        #union       
print(s1.union(s2)) #union
print(s1&s2)               #intersection
print(s1.intersection(s2)) #intersection
print(s1-s2) #set difference
print(s2-s1) #set difference
print(s1^s2) #symmetric diff union-intersection
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2)) 

print(set2)
fs=frozenset([1,2,3]) #takes as elements not as list
print(fs)