def bubble_sort(l):     
	d = len(l)      # определение длины списка
	for j in range(0, d-1):  # перебирает значение j от первого (нулевого) элемента до последнего (длина -1)
		for i in range (0, d-j-1): # перебирает значение i от нулевого до конечного с шагом -1
			if l[i]>l[i+1]: # сравнивает значения с рядом стоящим и меняет их местами. В итоге в ходе i-шага сортировки переносит наибольшие числа в конец списка и далее не трогает их т.к. (d-j-1)
				l[i], l[i+1] = l[i+1], l[i]
	return (l)
