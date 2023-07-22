class Person:
    def __init__(self):
        # 私有属性，外部不可以读写
        self.__age = 18
    # 使用方法让它可以被获取到，读权限放开
    
    ## property的作用是可以使用属性的方式来使用这个方法,可以保证隐私变量只读不写
    @property
    def age(self):
        print(self.__age)
        # return self.__age

p1 = Person()
# p1.age()
p1.age

# 方法被赋值会报错，达到不可写的目的
p1.age=666

# p1.age=19
# print(p1. age)