class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("父类中构造参数")

    def eat(self):
        print("%s is eatting"%self.name)

class Person(Animal):
    def __init__(self,name,age,sex,hobbies):
        super().__init__(name,age,sex)
        self.hobbies = hobbies
        print("子类中构造参数")
    def eat(self):
        super().eat()
        print("%s 在优雅的吃饭"%self.name)

    def hobby(self):
        print("%s 的爱好是: %s"%(self.name,self.hobbies))


p1=Person("owen",38,"F","women")
p1.eat()
p1.hobby()