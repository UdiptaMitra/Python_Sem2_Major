#tuple packing
t4='a','b','c' 
print(t4) #output - ('a','b','c')

#tuple unpacking
t5=1,2,3
x,y,z=t5 #no of var = no of elements otherwise value error
print(x,y,z) #x,y,z now have respective elements at resp positions

#extended unpacking
t6=1,2,3,4,5,6,7
a,*b=t6 
c,*d,e=t6
''' *var mane jotogulo normal variable ache sekhane values as per assigned,
rest of values go to *var as a LIST type data
unpacking e ordering of variables matter'''
print(a,b)
print(c,d,e)

'''swapping of two variables dumb way of doing things
a=10 b=20
temp=a
a=b
b=temp 
even if int takes less space than tuple but we dont care coz ample space in python 
and also both have same time complexity
'''
#swapping of two var using tuple pack unpack
a=10
b=20
a,b=b,a
'''intermediate step 
t=a,b (packing)
b,a=t (unpacking)'''
print(a,b)