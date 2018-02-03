n=int(input())
p=int(input())
f= open('data.txt', 'w+')
f.write('48 48 3 75 26 57 53 21 71 15')
f.seek(0)
x=format(f.read()).split(' ')
with open('out-1.txt', 'w') as o1:
    o1.seek(0)
    z = ""
    for y in x:
        if int(y)%n == 0:
            z = z + str(y) + ' '
    o1.write(z)
with open('out-2.txt', 'w') as o2:
    o2.seek(0)
    s = ""
    for y in x:
        y = int(y)**p
        s = s + str(y) + ' '
    o2.write(s)
f.close()
