def bin2dec(number):
    dec = 0
    number = str(number)
    s = len(number)
    f = s
    while s != 0:
        dec += int(number[f-s])*2**(s-1)
        s -= 1
    return(dec)

def oct2dec(number):
    dec = 0
    number = str(number)
    s = len(number)
    f = s
    while s != 0:
        dec += int(number[f-s])*8**(s-1)
        s -= 1
    return(dec)

def hex2dec(number):
    dec = 0
    number = str(number)
    s = len(number)
    number = number.lower()
    f = s
    hex16 = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
     'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    while s != 0:
        y = number[f-s]
        x = hex16[y]
        dec += x*16**(s-1)
        s -= 1
    return(dec)

def dec2bin(number):
    b = ""
    while number > 0:    
        o = number % 2
        number = number // 2
        b = str(o) + b    
    return(b)

def dec2oct(number):
    b = ""
    while number > 0:    
        o = number % 8
        number = number // 8
        b = str(o) + b    
    return(b)

def dec2hex(number):
    b = ""
    hex16 = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
     10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    while number > 0:    
        o = number % 16
        x = hex16[o]
        number = number // 16
        b = x + b    
    return(b)

