ls=[1,2,3,4]
print(ls.append(5)) #no return, adds elements from behind
print(ls)
print(ls.pop()) #returns last element also removes it
print(ls)
print(ls.remove(2)) #no return but remove element at specified position
print(ls)
ls1=[10,20,30,40]
ls2=[50,60,70,80]
print(ls1+ls2) #concat, no change in initial lists
print(ls1.extend(ls2)) #no return also change in ls1, no change in ls2
print(ls1,ls2)