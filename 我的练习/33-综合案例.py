import abc

class Animal(metaclass=abc.ABCMeta):
    def __init__(self,name,age=1):
        if not isinstance(age,int):
            raise "age must be int type"
        self.name = name
        self.age = age

    def eat(self):
        print("%s 在吃饭" % self)

    def play(self):
        print("%s 在玩" % self)

    def sleep(self):
        print("%s 在睡觉" % self)

    @abc.abstractmethod
    def work(self):
        pass


    

class Person(Animal):
    # 接受实例化传参，要一一对应
    def __init__(self,name,pets,age=1):
        super(Person,self).__init__(name,age)
        self.pets = pets

    def yangpet(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def work(self):
        self.make_pet_work()

    def make_pet_work(self):
        for pet in self.pets:
            pet.work()

    # __str__( )函数和__init__( )函数一样，都是python中的特殊函数，一般来说，打印对象会返回对象的地址，而地址信息通常对我们没有什么用，
    # 通过__str__( )函数可以打印对象的属性信息，方便我们调试代码
    def __str__(self):
        return "%s 今年 %s 岁" %  (self.name,self.age)

class Dog(Animal):
    def __init__(self,name,age=1):
        super(Dog,self).__init__(name,age)

    def work(self):
        print("%s 在看家" % self)

    # __str__( )函数和__init__( )函数一样，都是python中的特殊函数，一般来说，打印对象会返回对象的地址，而地址信息通常对我们没有什么用，
    # 通过__str__( )函数可以打印对象的属性信息，方便我们调试代码
    def __str__(self):
        return "小狗 %s 今年 %s 岁" %  (self.name,self.age)

class Cat(Animal):
    def __init__(self,name,age=1):
        super(Cat,self).__init__(name,age)

    def work(self):
        print("%s 在逮老鼠" % self)

    # __str__( )函数和__init__( )函数一样，都是python中的特殊函数，一般来说，打印对象会返回对象的地址，而地址信息通常对我们没有什么用，
    # 通过__str__( )函数可以打印对象的属性信息，方便我们调试代码
    def __str__(self):
        return "小猫 %s 今年 %s 岁" %  (self.name,self.age)

d = Dog("多多")
c = Cat("喵喵",3)
p = Person("小明",[d,c],16)
p.sleep()
p.yangpet()
p.make_pet_work()