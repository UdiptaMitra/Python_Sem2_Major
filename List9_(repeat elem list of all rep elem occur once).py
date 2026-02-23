#WAP python to check whether a given list contains any repeating element or not also print all repeating elements each only once

l1=[]
l1_rep=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i+1)+" "))
    l1.append(elem)
repeat_check=False
for i in range(n_list):
    if l1[i] not in l1_rep: #jodi already sei element ta oi repeat list e na thake tahole only add
        for j in range(i+1,n_list):
            if l1[i]==l1[j]:
                l1_rep.append(l1[i])
                repeat_check=True
                break
if repeat_check==False:
    print("no repitition")
else:
    print(l1_rep)

 #[1,2,3,2,3,2] - [2,3,2] problem appear - not in statment ta likhle problem gone