#wap to input a string and compress the string. eg- aaabbcccc - a3b2c4
str1=input("enter a string: ")
uniq_lett=[]
compress=""
for i in range(len(str1)):
    if str1[i] not in uniq_lett:
        uniq_lett.append(str1[i])
for i in range(len(uniq_lett)):
    count=str1.count(uniq_lett[i])
    compress+=uniq_lett[i]+str(count)
    count=""
print(compress)
            
