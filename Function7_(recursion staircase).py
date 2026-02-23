''' Climbing staircase with n steps each move - climb one step or two steps.
find in how many distinct ways you can reach top'''

'''def stairs(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return stairs(n-1)+stairs(n-2)
n=int(input("enter number of stairs: "))
print(stairs(n))'''
#top down dynamic programming approach

def stairs(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return 1
    else:
        memo[n]=stairs(n-1,memo)+stairs(n-2,memo)
    return memo[n]
n=int(input("enter number of stairs: "))
print(stairs(n))
