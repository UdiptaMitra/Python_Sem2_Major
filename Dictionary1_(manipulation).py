#set of key value pairs, key - immutable, unique, value - mutable, may not be unique
# elem accessed by key-value not indeces , key-value pair unique, overall elements unique
#access time is fast hashing function works just as in set

d={'a':1, 'b':2, 'c':2}
print(d['a'])
d1=dict(a=1,b=2) #constructor is used to create instance
print(d1)
#d1=dict((1,2)=1,(3,4)=2) - only string var names turn to keys no other things
d1['c']=5
print(d1)
del d['a']

t=(('a',1),('b',2)) #dictionary with tuple of tuples
print(dict(t))
l=[('a',1),('b',2)] #dictionary with list of tuples
print(dict(l))

key1=('a','b','c') #use 2 tuple, 2 list, one tuple one list
value2=(100,200,300)
d=dict(zip(key1,value2)) #zip
print(d)

d3=d #shallow copy
d4=dict(d) #deep copy


#traverse via keys
for i in d:
    print(d[i])
#traverse via values
for i in d.values():
    print(i)

for k,v in d1.items():
    print(k,v)
    
k=('a','b','c')
d=dict.fromkeys(k,0) # all keys have 0 as values
print(d)

#update method multiple key value pairs