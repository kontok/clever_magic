from string import digits, ascii_letters
import random

def password_generator(n):
    valid_values = list(digits + ascii_letters)
    while True:
        password = ''
        while len(password) != n:
            password+=random.choice(valid_values)
        yield password



