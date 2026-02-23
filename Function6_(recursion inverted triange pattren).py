def pattern(n,row=0):
    if row==n:
        return
    else:
        print(" "*row+"*"*(n-row))
    pattern(n,row+1)
n=int(input("enter a number: "))
pattern(n)

