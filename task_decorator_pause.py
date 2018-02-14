import time

def pause(s):
    def decorator(func):
        def wrapper (*args, **kwargs):
            time.sleep(s)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@pause(2)
def func():
    print('Фунция выполняется с задержкой 2 секунды!')
