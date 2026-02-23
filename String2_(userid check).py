#wap to input userid from user check whether the id follows the given pattern
#all char are uppercase the id starts with USER followed  by 3 digits followed by one special char followed by any number of char
digflag=1
userid=input("enter the user id")
if userid.isupper():
    if userid.startswith("USER"):
        for i in range(4,7):
            if userid[i].isdigit()==True:
                digflag*=1
            else:
                digflag*=0
        if digflag==1:
            if userid[7].isalnum()==False:
                flag=1
            else:
                flag=0
        else:
            flag=0
    else:
        flag=0
else:
    flag=0
if(flag==1):
    print("yes user id follows the pattern")
else:
    print("no user id not follows the pattern")

                