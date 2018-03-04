from abc import ABCMeta, abstractmethod
import time

class ValidatorException(Exception):
    def __init__ (self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class Validator(metaclass=ABCMeta):
    types = {}

    def __init__(self,sourse):
        self.sourse =sourse
    
    @abstractmethod
    def validate(self, value):
        """
        True or False
        """

    @classmethod
    def add_type(cls, name, klass):

        if not name:
            raise ValidatorException('Validator must have a name!')

        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))

        cls.types[name] = klass
        
    @classmethod
    def get_instance(cls, name):
        klass = cls.types.get(name)
        if klass is None:
            raise ValidatorException('Validator with name "{}" not found'.format(name))

        return klass(name)

class DateTimeValidator(Validator):
    def __init__(self, source):
        super().__init__(source)
    def validate(self, value):
        dt=["%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y",
            "%d/%m/%Y %H:%M", "%d-%m-%Y %H:%M", "%d.%m.%Y %H:%M",
            "%d/%m/%Y %H:%M:%S", "%d-%m-%Y %H:%M:%S", "%d.%m.%Y %H:%M:%S",
            "%Y/%m/%d", "%Y-%m-%d", "%Y.%m.%d",
            "%Y/%m/%d %H:%M", "%Y-%m-%d %H:%M", "%Y.%m.%d %H:%M",
            "%Y/%m/%d %H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y.%m.%d %H:%M:%S"]
        result = False
        for z in dt:
            try:
                if time.strptime(value, z):
                   result = True
            except ValueError:
                pass
        return result

class EMailValidator(Validator):
    def validate(self, value):
        if value.count('@') == 1:
            result = True
        else:
            result = False
        return result

Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)
"""
validator = Validator.get_instance("email")
print(validator.validate("info@itmo-it.org"))
print(validator.validate("undefined"))



validator = Validator.get_instance("datetime")
print(validator.validate("1.9.2017"))
print(validator.validate("01/09/2017 12:00"))
print(validator.validate("2017-09-01 12:00:00"))
print(validator.validate("undefined"))
"""
