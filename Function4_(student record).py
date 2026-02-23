''' given a list of students record define a user defined function is_eligible.
if students marks<30 return true, otherwise return false. list passed as argument
use function with filter operation to extract id of eligible student using lambda function with map
create new list with students id and updated marks where eligible students get grace marks of 5'''




student_record=[("730","Udipta",100),("749","Apabrita",40),("723","Iqran",0),("701","Srinjoy",25),("733","Sourasrota",80)]
'''def is_eligible(l1):
    flag=[]
    for i in l1:
        if i[2] < 30:
            flag.append("true")
        else:
            flag.append("false")
    return flag
flag=is_eligible(student_record)
print(flag)
id_eligible=[]
#id_eligible=list(map(lambda x:x=="true",flag))

for i in range(len(flag)):
    if flag[i]=="true":
        id_eligible.append(student_record[i][0])
print(id_eligible)
'''
new_update=[]
new_update=list(map(lambda x:(x[0],x[2]) if x[2]>30 else (x[0],x[2]+5),student_record))
print(new_update)


student_record=[("730","Udipta",100),("749","Apabrita",40),("723","Riya",0),("701","Parul",25),("733","Sourasrota",80)]
l4=[]
'''def funct(elem):
    if elem[2]<30:
        return True'''

'''for i in range(len(student_record)):
    print(funct(student_record[i]))'''

l4=list(filter(lambda x: x[2]<30,student_record))


    print(funct2(student_record[i]))
print(l4)

for i in range(len(l4)):
    print(l4[i][0])