# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     # 拦截实例对象创建过程
#     #     print("new: ",cls,args,kwargs)
#     # self 是 new函数传递过来的
#     def __init__(self):
#         # 实例对象创建之后，自动添加额外的属性或方法
#         print("初始化方法")
#         self.name = "sz"
#
#     def __del__(self):
#         # 当对象被释放时执行的方法
#         print("这个对象被释放了")
#
# p = Person()
# # del p
# print(p)
# print(p.name)


class Person:
    # 防止类外部修改，设置其为私有属性
    __count = 0
    def __init__(self):
        # 调用类属性1
        self.__class__.__count += 1
    # def __new__(cls, *args, **kwargs):
    #     # self.count += 1
    #     return cls
    def __del__(self):
        # 调用类属性2
        Person.__count  -= 1
    # @staticmethod，修饰的是类内部定义的独立函数方法即不带self的形式的方法
    # 定义类方法
    @classmethod
    def Count(cls):
        print(cls.__count)

p1 = Person()
p2 = Person()
p1.Count()
del p1
del p2
p3 = Person()
p3.Count()