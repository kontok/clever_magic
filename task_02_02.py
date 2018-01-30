def bubble_sort(l):
	d = len(l)
	for j in range(0, d-1):
		for i in range (0, d-j-1):
			if l[i]>l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
	print(l)
bubble_sort()
