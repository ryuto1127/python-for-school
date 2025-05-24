import math

def sphere_volume(r):
    return(4 / 3 * math.pi * r ** 3)
    
def hemisphere_volume(r):
    return(sphere_volume(r) / 2)
    
print(hemisphere_volume(1))