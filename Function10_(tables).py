#write  function for an integer and print its multiplication table upto 10
def multiplication(num):
    for i in range(1,11):
        print(num,"xn",i,"=",num*i)
num=int(input("Enter a number: "))
print("The multiplication table is as follows: ")
multiplication(num)
