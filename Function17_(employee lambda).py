employees=[
    {"name":"Amit","salary":50000,"dept":"IT"},
    {"name":"Anupam","salary":75000,"dept":"HR"},
    {"name":"Sara","salary":60000,"dept":"IT"},
    {"name":"David","salary":45000,"dept":"Finance"},
    {"name":"John","salary":50000,"dept":"IT"}
]
it_employee=list(filter(lambda x: x["dept"]=="IT",employees))
#extract names of it employees
l9=list(map(lambda x: x["name"],filter(lambda x: x["dept"]=="IT",employees)))
print(l9)
#bonus of 10% for it employees
l10=list(map(lambda x: x["salary"]*0.1,it_employee))
print(l10)
#return name of employees whose bonus is greater than 5000
l11=list(map(lambda x: x["name"],filter(lambda x: x["salary"]*0.1>=5000,it_employee)))
print(l11)
