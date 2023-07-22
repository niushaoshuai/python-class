#!/usr/bin/env python

class Peopel:
    # 类属性，如果实例中没有定义，那么通过实例访问递归地也能访问到类属性。公用同一个内存空间
    nationality = "TW"
    def __init__(self,name,age,sex):
        self.name = name
        self.sex = sex
        self.age = age

p1 = Peopel("jj",18,"F")
p2 = Peopel("jj1",20,"F")
p3 = Peopel("jj1",21,"M")

print(p3.__dict__)

print(p1.nationality)
print(Peopel.nationality)
Peopel.nationality="CN"
# 实例属性，从类属性中继承而来，如果被修改则只对当前实例生效这时会独立存放单独的内存空间
print(p1.nationality)
print(Peopel.nationality)   
p1.nationality="JP"
print(p1.nationality) 
print(p2.nationality) 
