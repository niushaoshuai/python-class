import abc

# 声明为抽象类，抽象类不可被调用
class Animal(object,metaclass=abc.ABCMeta):
    # 声明为抽象方法，抽象方法不可被调用,子类必须实现
    @abc.abstractmethod
    def jiao(self):
        pass
    # 声明为抽象类方法，抽象类方法不可被调用，子类必须实现
    @abc.abstractclassmethod
    def test(cls):
        pass

class Dog(Animal):
    def jiao(self):
        print("汪汪")

    @classmethod
    def test(cls):
        print("汪xxxxxx")

class Cat(Animal):
    def jiao(self):
        print("喵喵")

    @classmethod
    def test(cls):
        print("喵xxxxxx")

# 不同对象调用同一个方法产生不同结果，这叫多态
def test(obj):
    obj.jiao()

c = Cat()
d = Dog()
# a = Animal()
test(c)
Dog.test()
Cat.test()