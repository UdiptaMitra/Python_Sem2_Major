'''An electricity board charges customers according to the following tariff rules:
 First 100 units → ₹1 per unit
 Next 100 units (101-200) → ₹2 per unit
 Remaining units (above 200) → ₹5 per unit
Write a Python program that:
I. Accepts the total number of units consumed from the user.
II. Uses nested if-else statements to calculate the electricity bill.
III. Displays a clear breakdown of the bill calculation, showing:
o Units charged in each slab
o Cost of each slab
o Total electricity bill amount'''


def bill(unit):
    if unit<=100:
        amt=unit*1
        print("Slab 1; Rate- Rs1/unit for first 100 units; Units consumed-",unit,"; amount in this slab ",(1*unit))
    else:
        if (unit>100) & (unit<=200):
            amt=100*1 + 2*(unit-100)
            print("Slab 1; Rate- Rs1/unit for first 100 units; Units consumed-100; amount in this slab ",(1*100))
            print("Slab 2; Rate- Rs2/unit for next 100 units; Units consumed-",unit-100,";amount in this slab ",(2*(unit-100)))
        else:
            amt= 100*1 + 100*2 + 5*(unit-200)
            print("Slab 1; Rate- Rs1/unit for first 100 units; Units consumed-100; amount in this slab ",(1*100))
            print("Slab 2; Rate- Rs2/unit for next 100 units; Units consumed-100; amount in this slab ",(2*100))
            print("Slab 3; Rate- Rs5/unit for above 200 units; Units consumed-",unit-200,"; amount in this slab ",(5*(unit-200)))
    return amt

unit=float(input("Enter the units consumed: "))
amt=bill(unit)        
print("The total bill amount is ",amt)
    