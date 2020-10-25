def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class SomeClass:

    def some_method(self):
        print('Some Method!!!')


a = SomeClass()
print(id(a))
a.some_method()
print()
b = SomeClass()
print(id(b))
b.some_method()
