JPEG_MB = 1.5
GIGABYTE = 1024
flashed_space = 16
photo100_space_giga = (100 * JPEG_MB) / GIGABYTE


def space_left(number_of_photos):
    return(flashed_space - (number_of_photos / 100 * photo100_space_giga))
    
print(space_left(100))