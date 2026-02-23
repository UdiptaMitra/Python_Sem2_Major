#wap to create user defined function to count digitsa of a number
def count_dig(num):
    count=0
    while(num>0):
        count+=1
        num=num//10
    return count
num=int(input("enter a number: "))
print("the number of digits in the given number is: ",(count_dig(num)))