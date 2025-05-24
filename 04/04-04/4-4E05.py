import math

def area_circle_def(a, b):
    small = math.pi * (a ** 2)
    big = math.pi * (b ** 2)
    return(big - small)
    
print(area_circle_def(5, 6))