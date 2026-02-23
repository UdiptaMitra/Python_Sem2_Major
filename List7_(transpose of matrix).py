l1=[[1,2,3],[4,5,6]]     
n_col=len(l1[0])
n_row=len(l1)
t_l=[]#traversing by column 
for i in range(n_col):
    row=[]
    for j in range(n_row):
        row.append(l1[j][i])
    print(row)
    t_l.append(row)
print(t_l)
#full form version above one line below
t_l=[[l1[j][i] for j in range (n_row)] for i in range(n_col)]
print(t_l)