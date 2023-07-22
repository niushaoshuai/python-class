# -*- coding:utf-8 -*-
# class Person:
#     pass

# # py3默认是新类,py2如果不显式引用object则默认为经典类
# print(Person.__base__)

# # property 使用方式1
# class Person(object):
#     # 隐私变量默认在类的外部不可访问
#     def __init__(self):
#         self.__age = 18

#     def get_age(self):
#         return self.__age

#     def set_age(self,value):
#         self.__age = value

#     age = property(get_age,set_age)

# p1 = Person()
# print(p1.age)

# p1.age = 90

# print(p1.age)

# print(p1.__dict__)

# # property 使用方式2
# class Person(object):
#     def __init__(self):
#         self.__age = 18

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self,value):
#         self.__age = value

# P1 = Person()
# print(P1.age)

# P1.age = 90
# print(P1.age)

# print(P1.__dict__)


# property 把类的方法当属性来使用，确保类的属性被安全规范的被使用


#################### property在经典类中的使用,在py2测试 #################### 
# # property 使用方式1
# class Person:
#     def __init__(self):
        
#         self.__age = 18

#     def get_age(self):
#         print("________get")
#         return self.__age

#     def set_age(self,value):
#         print("________set")
#         self.__age = value

#     age = property(get_age,set_age)
#     pass

# p = Person()
# print(p.age)

# # 会增加一个变量
# p.age = 90
# print(p.age)

# # {'age': 90, '_Person__age': 18}
# print(p.__dict__)

# # proper只管读取

# property 使用方式2
class Person:
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        print("________get")
        return self.__age

    @age.setter
    def age(self,value):
        print("________set")
        self.__age = value

P=Person()
print(P.age)
print(P.__dict__)
P.age=20

print(P.age)

print(P.__dict__)

# # proper只管读取,不管写。因此以后尽量使用新式类