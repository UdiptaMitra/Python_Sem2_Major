#remove occurance of 7 from the given tuple and create a new tuple
tup1=(4,7,2,7,9,2,5,7)
tup2=()
for i in tup1:
    if i==7:
        continue
    else:
        tup2+=(i,)
        #tup2.append(i) #append not work for tuple as its immutable
print(tup2)

#also u can turn it to list and use pop

'''i=1
t1=(i)
print(type(t1)) #- its int not tuple
#convert int to tuple
t2=(i,) #instance creation of tuple type of object
print(type(t2)) #- its tuple'''