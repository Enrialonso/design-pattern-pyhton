#Design Pattern: Singleton

Singleton is possibly the simplest pattern that exists, this patter allow create a single instance of a class and restrict 
the new instances creation. This is usefull, for example if you are interested to control the instances creation for 
connection to a resource, whit this patter you guarantee the access to the resources from a unique instance arround the all code.

####Uses case:
- **Logger:** normaly in an aplication use the logs with the same configuration and access to the same file for write the traces for the program,
in this case, you need a unique point of access to manage the writing the traces and avoid the issues if many instances try to log
at the same time on the file. This pattern restric that and allow a unique point of access.

- **Configuration file:** is a good practice group the configurations on a single file and read on the start of the application. 
everybody knows that the disk reading is an expensive operation and if you can read one time and load this data on an 
instance in memory is better for performance that read all time form the disk. Singleton can improve a lot this and is 
the most strong uses cases for this pattern.

- **Cache:** in the previous case comment to the how is important load the config file on memory and read from the memory. 
In this uses case its similar but oriented to cached data from any type of requests. Use the instance of a class for store 
the data and no access for another slowest resources. Is better and quikly access to the memory than another resources.

- **Data base pool access:** if your application need access to a database and also need centralize de access this pattern 
allow restrict the access along the aplication to only one instance, donts matter how many intances are created, all 
databesa access is driven for the same class instance.

####Python implementation:

Without arguments on `__init__`

```python
class Singelton:
    __instance = None

    def __new__(self):
        if self.__instance is None:
            self.__instance = super().__new__(self)
        return self.__instance

    def __init__(self):
        self.attr = 10

    def sample_method(self):
        print(f'sample_method!!!')

    def print_attr(self):
        print(f'attr = {self.attr}')

a = Singelton()
print(f'class id = {id(a)}')
a.print_attr()
a.sample_method()
b = Singelton()
print(f'class id = {id(b)}')
b.sample_method()
b.print_attr()
print(f'a == b: {a == b}')

```

Output code:

```shell script
class id = 140394913705360
attr = 10
sample_method!!!

class id = 140394913705360
sample_method!!!
attr = 10

a == b: True
```

On the previous implementation use the magic method of `__new__` for verify if the instance is created based on the value 
of private attr `__insatance`.

- If is the first time of the instance the class Singleton `__instance` is equal to `None` and  go into the `if` and 
instance the class with `super` method, load the class on `__instance` and return the instance of the class.

- In the second instance of the class Singleton the value of `__instance` is not `None` and directly return of the previous
class instance.

with arguments on `__init__`:

```python
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
```
 Output:
 
 ```shell script
class id = 140401281764944
attr = attr #1
sample_method!!!

class id = 140401281764944
sample_method!!!
attr = attr #2

a == b: True
```

When pass an arguments for the instance of the class you can need know per any new instance with new the values of the 
arguments, the arguments on the class instance the class change and maeby you don't want this on your code. A solution 
for this is better no pass arguments to the class or take care if you instance the class in another parts of the code 
ensure instance with the same values on the frist instance of the class.

##Others Implementations:

####By Heritage:

```python
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
```
Output:
```shell script
140569226808400
Some Method!!!

140569226808400
Some Method!!!
```

####By Decorator:

```python
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
```
Output:
```shell script
139761878994192
Some Method!!!

139761878994192
Some Method!!!
```




