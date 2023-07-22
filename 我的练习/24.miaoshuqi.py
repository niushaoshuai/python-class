#-*- coding: utf8 -*-
# ###### 经典类无法使用描述器，新式类才可以
# class Age(object):
#     def __get__(self,instance,owner):
#         print("get")
        
#     def __set__(self,instance,owner):
#         print("set")

#     def __delete__(self,instance):
#         print("delete")

# class Person(object):
#     age = Age()
#     # 会劫持描述器中的__get__方法
#     def __getattribute__(self,instance):
#         print("xxx")

# ####### 通过实例去操作描述器,而不是通过类去操作
# p = Person()
# p.age = 10
# print(p.age)

# # print(Person.age)
# # Person.age = 10
# # del Person.agepr

# 资料描述器： 实现了get\set
# 非资料描述器 仅仅实现了get
# 优先级： 资料描述器 > 实例属性 >非资料描述器


# class Age(object):
#     def __get__(self,instance,owner):
#         print("get")
        
#     def __set__(self,instance,owner):
#         print("set")

#     def __delete__(self,instance):
#         print("delete")

# class Person(object):
#     age = Age()
#     # 会劫持描述器中的__get__方法
#     def __init__(self,age):
#         self.age = age

# ####### 通过实例去操作描述器,而不是通过类去操作
# p = Person(9)
# p.age = 10
# print(p.age)
# print(p.__dict__)


# ----------------------------描述器-值的存储问题------------------------------------
class Age(object):
    def __get__(self,instance,value):
        # print("get",self,instance,value)
        return instance.value
        
        
    def __set__(self,instance,value):
        # print("set",self,instance,value)
        instance.value = value

    def __delete__(self,instance):
        # print("delete")
        del instance.value

class Person(object):
    age = Age()

p = Person()
p.age = 18
p1 = Person()
p1.age = 19
print(p.age,p1.age)
del p.age 
del p1.age
# print(p.age,p1.age)