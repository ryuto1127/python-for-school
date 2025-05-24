TOILET_ONCE = 6
DISHWASHER = 19
SHOWER = 7

def total_liters(toilet, dishes, shower):
    return(toilet * TOILET_ONCE + dishes * DISHWASHER + shower * SHOWER)
    
print(total_liters(10, 2, 10))