#wap to input a list and find position of all unique elements in the list. list of tuple. (elem, [list of position])
l1=[]
l1_rep=[]
l1_pos_dist=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    l1.append(elem)

for i in range(n_list):
    l_pos=[i]
    if l1[i] not in l1_rep:
        for j in range(i,n_list):
            if (l1[i]==l1[j]) and (i!=j):
                l_pos.append(j)
                l1_rep.append(l1[i])
        l1_pos_dist.append((l1[i],l_pos))
print(l1_pos_dist)