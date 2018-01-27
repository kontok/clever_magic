god = int(input())
if (god % 100 == 0 and god % 400 != 0) or (god % 4 != 0):
    print ('no')
else:
    print ('yes')
