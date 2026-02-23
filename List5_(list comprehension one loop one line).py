l1=list(range(11))
l2=[i*2 for i in l1]
print(l2)
#ei dutor output same
l3=[]
for i in l1:
    l3.append(i*2)
print(l3)

#positive element extraction
l1=[-4,-2,0,7,8]
p_l1=[i for i in l1 if i>0]
print(p_l1)

#absolute value of each element
a_l1=[abs(i) for i in l1]
print(a_l1)

l1=[' apple',' banana ','orange ']
c_l1=[i.strip() for i in l1]
print(c_l1)

#create a list of tuples where the second elent is square of first one
s_t=[(x,x**2) for x in range(6)]
print(s_t)