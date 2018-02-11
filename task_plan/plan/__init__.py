import sys

from plan import storage


get_connection = lambda: storage.connect('task_plan.sqlite')


def action_add():
    """Добавить задачу"""
    task = input('\nВведите задачу: ')

    with get_connection() as conn:
        task = storage.add_task(conn, task)

    print('Задача введена: {}'.format(task))

def action_find_all():
    """Вывести все задачи"""
    with get_connection() as conn:
        tasks = storage.find_all(conn)

    for task in tasks:
        template = '{task[id]} - {task[task]} - {task[status]} - {task[created]}'
        print(template.format(task=task))

def actin_now():
    """Вывести текущие задачи"""
    with get_connection() as conn:
        tasks = storage.find_task_by_status(conn, status)
        for task in tasks:
            template = '{task[id]} - {task[task]} - {task[status]} - {task[created]}'
            print(template.format(task=task))


def action_edit_status():
    """Изменить статус"""
    pk = input('Введите номер задачи: ')
    s =''
    with get_connection() as conn:
        status = storage.edit_status(conn, s, pk)
    print('Статус изменён')

def action_edit_task():
    """Редактирование задачи"""
    pk = input('Введите номер задачи: ')
    with get_connection() as conn:
        t = storage.find_task_pk(conn, pk)
        task = storage.edit_task(conn, t, pk)

def menu():
    """Показать меню"""
    print('''
Список команд:
1. Добавить задачу.
2. Вывести список задач.
3. Редактировать задачу.
4. Изменить статус задачи.
q. Выход.
''')


def exit_prog():
    """Выход"""
    sys.exit(0)

plan = {
    '1': action_add,
    '2': action_find_all,
    '3': action_edit_task,
    '4': action_edit_status,
    'q': exit_prog,
    'm': menu
    }

def main():
    with get_connection() as conn:
        storage.initialize(conn)
    print('Привет, чем займемся?') 

    menu()

    while 1:
        cmd = input('\nВведите команду: ')
        action = plan.get(cmd)

        if action:
            try:
                action()
            except Exception as e:
                print(e)
        else:
            print('Не верная команда. Вывести список команд "m"')
