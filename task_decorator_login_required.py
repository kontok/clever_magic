import hashlib

is_logined = 0

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

def login_required(func):
    def wrapper(*args, **kwargs):
        global is_logined
        if is_logined == 1:
            return func(*args, **kwargs)
        x = 0
        while x<3:
            username = input()
            password = input()
            with open('token.txt', 'a+') as f:
                f.seek(0)
                print(make_token(username, password))
                if f.read() == make_token(username, password):
                    is_logined = 1
                    return func(*args, **kwargs)
            x += 1
        return None
    return wrapper


"""
with open('token.txt', 'w') as f:
    f.write(make_token('user', 'password'))

@login_required
def f1():
    print('Функция защищена паролем')


@login_required
def f2():
    print('Эта функция тоже защищена паролем')


f1()
f2()
f1()
"""
