def get_free_land(land, garden_bed):
    m = str(land[1])
    m = float(m[0]) / float(m[2])
    land_s = land[0]*m*100
    if land_s == 0:
        raise ValueError("Не задана площадь участка")
        
    garden_bed_s = garden_bed[0]*garden_bed[1]
    if garden_bed_s == 0:
        raise ValueError("Не задана площадь грядки")
    
    if land_s <garden_bed_s :
        raise ValueError("Размер грядки больше размера участка")        

    return land_s % garden_bed_s

