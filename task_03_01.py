from datetime import datetime, date

def get_days_to_new_year():
    x = datetime.today() # текущая дата
    y = datetime(x.year +1, 1, 1, 0, 0, 0) # следующий Новый год
    d = (y - x).days # разница в днях
    return d




