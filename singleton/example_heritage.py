class Singleton(object):
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]


class SomeClass(Singleton):

    def some_method(self):
        print('Some Method!!!')


a = SomeClass()
print(id(a))
a.some_method()
print()
b = SomeClass()
print(id(b))
b.some_method()
