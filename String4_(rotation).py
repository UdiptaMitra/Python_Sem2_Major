'''a string is said to be a rotation of another string if it can be obtained by shifting 
char from beginning to the end without changing order given s1 and s2 determine whether 
s2 is a rotation of s1. s1=abcd s2=cdab yes'''
str=input("enter a string: ")
str2=input("another string")
#method 1
flag=0
for i in range(len(str)):
    start=str[0]
    mid=str[1:len(str)]
    final=mid+start
    if final==str2:
        flag=1
    str=final
    mid=""
    start=""
if flag==1:
    print("yeahh")    
else:
    print("nayy")
#method 2  - more efficient
''' if str2 in (str+str): 
        print("yeahh")    
    else:
        print("nayy") '''