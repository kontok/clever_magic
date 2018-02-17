def get_quadrant_number(x, y):
    if x == 0 or y == 0:
        raise ValueError
    if x>0:
        if y>0:
            z = 1
        else:
            z = 4
    else:
        if y>0:
            z = 2
        else:
            z = 3
    return z

