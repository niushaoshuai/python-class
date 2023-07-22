class Person:
    age = 0
    # 实例方法
    def shlff(self):
        print(self)
        print(self.age)
        print(self.num)

    # 类方法
    @classmethod
    def lff(cls):
        print(cls)
        print(cls.age)
        # 访问实例属性会报错
        # print(cls.num)
    
    # 静态方法
    @staticmethod
    def jtff():
        print(Person.age)

p = Person()
p.num = 10

# ************* 类属性通过类或者实例都可以被访问
# 类属性
# print(Person.age)
# print(p.age)

# ************* 实例属性和方法只有实例才可以访问
# 实例属性
# print(p.num)


# p.shlff()

# ************* 类方法通过类或者实例都可以被访问
# p.lff()
# Person.lff()

# ************* 静态方法通过类或者实例都可以被访问,静态方法里面获取不到实例属性
# Person.jtff()
p.jtff()