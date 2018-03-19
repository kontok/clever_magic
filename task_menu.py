from abc import ABCMeta, abstractmethod

class CommandException(Exception):
    def __init__ (self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class Command(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self):
        pass

class Menu(object):
    commands = {}

    def __init__(self):
        self.num = 0
    def __iter__(self):
        self.__copy = self.__commands.copy()
        return self

    def __next__(self):
        while self.__copy:
            return self.__copy.popitem()
        raise StopIteration

    @classmethod
    def add_command(cls, name, klass):

        if not name:
            raise CommandException('Command must have a name!')
        elif not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))

        cls.types[name] = klass
        
    @classmethod
    def execute(cls, name):
        klass = cls.commands.get(name)
        if klass is None:
            raise CommandException('Command with name "{}" not found'.format(name))

        return klass(name)

class ShowCommand(Command):
    def __init__(self, task_num):
        self.task_num = task_num


    def execute(self):
        pass


class ListCommand(Command):

    def __init__(self):
        pass

    def execute(self):
        pass
