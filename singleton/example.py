class Singelton:
    __instance = None

    def __new__(self, attr):
        if self.__instance is None:
            self.__instance = super().__new__(self)
        return self.__instance

    def __init__(self, attr):
        self.attr = attr

    def sample_method(self):
        print(f'sample_method!!!')

    def print_attr(self):
        print(f'attr = {self.attr}')


a = Singelton('attr #1')
print(f'class id = {id(a)}')
a.print_attr()
a.sample_method()
b = Singelton('attr #2')
print(f'class id = {id(b)}')
b.sample_method()
b.print_attr()
print(f'a == b: {a == b}')
