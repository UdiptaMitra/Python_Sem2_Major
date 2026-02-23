#wap to input a list and find the frequency of each element. list of tuples (elem,freq)
l1=[]
l1_rep=[]
freq_dist=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    l1.append(elem)

#with using an extra list l1_rep
'''for i in range(n_list):
    if l1[i] not in l1_rep:
        count=0
        for j in range(i,n_list):
            if l1[i]==l1[j]:
                l1_rep.append(l1[i])
                count+=1
        freq_dist.append((l1[i],count))
print(freq_dist)'''

#without using an extra list l1_rep
for i in range(n_list):
    count=0
    if l1[i] not in l1[:i]: #er aage obdhi repeat koreni number ta extra list ta na niye korchi
        for j in range(i,n_list):
            if l1[i]==l1[j]:
                count+=1
    if count>0:
        freq_dist.append((l1[i],count))
print(freq_dist)
            
