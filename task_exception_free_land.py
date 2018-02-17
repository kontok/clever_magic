def get_free_land():
    land = eval(input())
    garden_bed = eval(input())
    land_s = land[0]*land[1]*10
    if land_s == 0:
        raise ValueError("Не задана площадь участка")
        
    garden_bed_s = garden_bed[0]*garden_bed[1]
    if garden_bed_s == 0:
        raise ValueError("Не задана площадь грядки")
    
        
    if land[0]*10 < garden_bed[0] or land[1]*10 < garden_bed[1]:
        if land[1]*10 < garden_bed[0] or land[0]*10 < garden_bed[1]:
            raise ValueError("Размер грядки больше размера участка")        
        
    while land_s > garden_bed_s:
        land_s -= garden_bed_s
    return land_s

get_free_land()
