#wap to input a string and find the largest palindromic substring palindromic substrings
str=input("enter a string: ")
max=0
pali=[]
pali2=[]
for i in range(len(str)):
    for j in range(i+1):
        sub=str[j:i+1]
        if sub==sub[::-1]:
            if len(sub)>=max:
                max=len(sub)
                pali.append(sub)
for i in pali:
    if len(i)==max:
        pali2.append(i)                
print(max)
print(pali2)
        