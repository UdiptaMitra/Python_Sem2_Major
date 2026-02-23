#wap to take latitude and longitude of n cities and store the coordinates as key
# and name of city as values store in dictionary

n=int(input("enter the total number of cities"))
coord_list=[]
name_list=[]
for i in range(n):
	lat=int(input("latitude "+str(i+1)+" :"))
	long=int(input("longitude "+str(i+1)+" :"))
	name=input("enter name of the city "+str(i+1)+" :")
	coord=(lat,long)
	coord_list.append(coord)
	name_list.append(name)

dict1=dict(zip(coord_list,name_list))
print(dict1)