class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        #1、 定义私有属性
        self.__life_val = 100 
        # print(self.__life_val)
    def get_life_val(self):
        # 私有变量在class类内部可以被访问,因此外部可以通过class类内部的方法来获取
        return self.__life_val

    def get_attack(self):
        self.__life_val -= 20
        print("%s 被攻击了，生命值-20"%self.name)
        self.__breath()
        return self.__life_val
    #2、 定义私有方法
    def __breath(self):
        print("%s is breathing"%self.name)


p1 = Person("owen",18,"F")
print(p1.get_life_val())
# 私有变量在class类外部不可以被访问
# p1.__life_val
p1.get_attack()
# 私有方法在class类外部不可以被访问
# p1.__breath()
# 通过如下方法也能访问私有方法或者变量，但不经常用
p1._Person__breath()
print(p1._Person__life_val)