x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = (x2-x1)**2 + (y2-y1)**2
b = (x3-x2)**2 + (y3-y2)**2
c = (x1-x3)**2 + (y1-y3)**2
if (a == c+b) or (c == a+b) or (b == a+c):
    print('yes')
else:
    print('no')
