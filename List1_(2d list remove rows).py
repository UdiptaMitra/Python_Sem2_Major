#Wap to input a 2d list 4x5 and remove its 2nd and 3rd rows
list1=[]
for i in range(4):
    list2=[]
    for j in range (5):
        temp=int(input("enter element "+str(i)+str(j)+" :"))
        list2.append(temp)
    list1.append(list2)
print(list1) #show initial list
del list1[1:3] #remove 2nd and 3rd row
print(list1)