import os.path as Path
import sqlite3

from .converter import convert, inverse


SQL_SELECT_ALL = '''
    SELECT
        id, task, status, created
    FROM
        plan
'''

SQL_SELECT_TASK_BY_PK = SQL_SELECT_ALL + ' WHERE id=?'

SQL_INSERT_TASK = '''
    INSERT INTO plan (task) VALUES (?)
'''

SQL_SELECT_STATUS_BY_PK = '''
    SELECT status FROM plan WHERE id=?
'''

SQL_UPDATE_STATUS = '''
    UPDATE plan SET status=? WHERE id=?
'''

SQL_UPDATE_TASK = '''
    UPDATE plan SET task=? WHERE id=?
'''


def dict_factory(cursor, row):
    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


def connect(db_name=None):
    """Устанавливает соединение с БД"""
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


def initialize(conn, creation_script=None):
    """Иницилизирует структуру БД"""
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__), 'resourses', 'schema.sql')

    with conn, open(creation_script) as f:
        conn.executescript(f.read())

def find_all(conn):
    """Все задачи"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
        return cursor.fetchall()

def add_task(conn, task):
    """Добавить задачу"""
    
    if not task:
        raise RuntimeError('Поле задача не может быть пустым')

    with conn: 
        cursor = conn.execute(SQL_INSERT_TASK, (task,))
        pk = cursor.lastrowid
    return task

def find_task_pk(conn, pk):
    """Найти задачу по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
        return cursor.fetchone()

def edit_task(conn, t, pk):
    """Изменяет статус задачи"""
    with conn:
        t = input('Введите новое описание задачи: ')
        if not t:
            raise RuntimeError('Поле задача не может быть пустым')
        conn.execute(SQL_UPDATE_TASK, (t, pk,))
        print('Задача отредактирована')
    return True


def edit_status(conn, s, pk):
    """Изменяет статус задачи"""
    with conn:
        while s != 'X' and s != 'V':
            s = input('Введите новый статус задачи (X - не выполнена / V - выполнена): ')
        conn.execute(SQL_UPDATE_STATUS, (s, pk,))
    return True


