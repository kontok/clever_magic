from string import digits, ascii_letters
import random

def password_generator(n):
    password = ''
    x =''
    valid_values = digits + ascii_letters
    while n !=0:
        x = random.choice(valid_values)
        password+=x
        n-=1
    yield password
    




        
