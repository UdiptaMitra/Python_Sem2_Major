#WAP python to check whether a given list contains any repeating element or not
# eg - [1,2,3,4] - false; [1,2,3,2] - true;
l1=[]
n_list=int(input("enter total number of elements in the list "))
for i in range(n_list):
    elem=int(input("enter element "+str(i)+" "))
    l1.append(elem)
repeat_check=False
flag=0
for i in range(n_list):
    #current_elem=l1[i]
    print("i "+str(i))
    for j in range(i+1,n_list):
        print("j "+str(j))
        if l1[i]==l1[j]:
            flag=1
            print(l1[i]) #prints the first repeated element
            repeat_check=True
            break
    if repeat_check==True: #breaks the loop just after repitition found no extra loop run
        break
#print(repeat_check)
if flag==0:
    print("no repitition")
     

