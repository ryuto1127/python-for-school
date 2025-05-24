QUARTER = 25
DIME = 10
NICKEL = 5

def convert_dollars(quarters, dimes, nickels):
    return((quarters * QUARTER + dimes * DIME + nickels * NICKEL) / 100)
    
print(convert_dollars(2, 4, 0))