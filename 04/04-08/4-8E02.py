def box_volume(a, b, c):
    return(a * b * c)
    
def box_number(a, b, c):
    return((590 * 236 * 276) / box_volume(a, b, c))
    
print(box_number(8, 12, 10))