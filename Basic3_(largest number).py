#wap to input 3 numbers and find the greatest of them all
a=int(input("enter the first num: "))
b=int(input("enter the second num: "))                                                                         
c=int(input("enter the third num: "))      

if a>b:
    if a>c:
        print("largest is ",a)
    else:
        print("largest is ",c)
else:
    if b>c:
        print("largest is ",b)
    else:
        print("largest is ",c)