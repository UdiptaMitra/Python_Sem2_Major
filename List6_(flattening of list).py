#2d list (3x3) flattened to 1d list (9x1)
l1=[[1,2,3],[4,5,6],[7,8,9]] 
#flattening of list
for row in l1:
    print(row)
    for elem in row:
        print(elem,end=' ')
print("\n")
f_1=[elem for row in l1 for elem in row]
print(f_1) 
