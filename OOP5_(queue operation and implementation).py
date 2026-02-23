class queue:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
        print(self.items)
    def remove(self):
        del self.items[0]
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
list1=queue()
while(True):
    ch=int(input("enter 1 for adding element, 2 for removing element, 3 for checking empty or not, 4 for finding the size,5 for displaying the list: "))
    if(ch==1):
        while(True):
            val=int(input("enter an element "))
            list1.push(val)
            flag=input("add more? y/n")
            if(flag=='y' or flag=='Y'):
                continue
            else:
                break
    elif(ch==2):
        while(True):
            list1.remove()
            flag=input("remove more? y/n")
            if(flag=='y' or flag=='Y'):
                continue
            else:
                break    
    elif(ch==3):
        print("empty?",list1.isEmpty())
    elif(ch==4):
        print("size is ",list1.size())
    elif(ch==5):
        list1.display()
    else:
        print("wrong input")
    flag2=input("any more functions? y/n")
    if(flag2=='y' or flag2=='Y'):
        continue
    else:
        break