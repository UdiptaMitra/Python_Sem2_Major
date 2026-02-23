'''global and local'''

var1=5 #global variable
def ABC():
    var2=10 #local variable
    #var1=100 #no change in initial var1 as this var1 is a new object with local scope
    #also local var override global var (scope overriding wrt variable - shadowing)
    global var1
    var1=10 #changed value (to update mentiopn keyword global)
    print(var2)
    print(var1)
    print(locals())
    print("var1 in locals?","var1" in locals())
    print("var2 in locals?","var2" in locals())
ABC()
print(var1)
#print(var2) - error shown as its local var
print(globals())
#globals() - namespace of all global variable
#locals () jodi main e di will give output of global
# onno function er modhye dile key value pairs of local variables

'''enclosed'''
def outer():
    #the initial x variable in outer is enclosed scope varible for inner -
    # - we can use it in inner even if its not local to inner but we cant update it
    x=10 #local scope wrt to outer function (not for inner) even if we can print it
    def inner():
        nonlocal x
        x=20 #nonlocal variable use korle we can update
        #x=20 #local wrt to inner (var overriding)
        print(x)
    inner()
    print(x) #value of x not updated even if its updated in inner
outer()

'''built in'''
#built in funtions like print input len etc are built in variables 
# and we are not allowed to override them
#print=4 is not alowed



