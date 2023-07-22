#_*_encoding:utf-8_*_
# class Person:
#     pass

# p1 = Person()
# p2 = Person()

# print(p1,p2)

# print(hex(id(p1)),hex(id(p2)))


# import sys

# class Person:
#     pass

# p1 = Person()
# print(sys.getrefcount(p1)-1)
# p2 = p1
# print(sys.getrefcount(p1)-1)

# del p2
# print(sys.getrefcount(p1)-1)
# del p1
# print(sys.getrefcount(p1)-1)


import sys

# class Person:
#     pass

# p1 = Person()
# print(p1)
# print(sys.getrefcount(p1)-1)

# # # 函数使实例指针+2 ，函数执行完增加的计数就会恢复之前
# # def log(obj):
# #     print(sys.getrefcount(p1)-1)

# # log(p1)

# # for attr in dir(log):
# #     print(attr,getattr(log,attr))

# # 当一个像当作另外一个对象引用元素时，指针+1
# l = [p1]

# print(sys.getrefcount(p1)-1)

# 内存管理机制 = 引用计数器机制 + 垃圾回收机制
# 引用计数器机制：当一个对象, 如果被引用 + 1, 删除一个引用 : -1 0: 被自动释放
# import objgraph
# class Person:
#     pass
# class Dog:
#     pass

# p = Person()
# d = Dog()

# # 可以查看, 垃圾回收器, 跟踪的对象个数
# # 同sys.getrefcount ，不同的是这里操作对象是一个类名
# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))

# p.pat = d 
# d.master = p 


# del p 
# del d 

# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))

# import sys
# class Person:
#     pass
# class Dog:
#     pass
# p = Person()
# l = [p]
# t = (p)

# d = Dog()
# p.pet = d
# d.master = p

# num = True
# # num.age = 10
# print(sys.getrefcount(p)-1)
# print(sys.getrefcount(d)-1)

# # ---------------------------------垃圾回收机制-分代回收---------------------------------------

# # python中默认把所有对象分成三代。第0代包含了最新的对象，第2代则是最早的一些对象。在一次垃圾回收中，所有未被回收的对象会被移到高一代的地方。
# import gc

# # 这个方法返回的是(700,10,10)，这也是gc的默认值。这个值的意思是说，在第0代对象数量达到700个之前，不把未被回收的对象放入第一代；而在第一代对象数量达到10个之前也不把未被回收的对象移到第二代
# print(gc.get_threshold())

# gc.set_threshold(200,5,5)
# print(gc.get_threshold())


# ---------------------------------垃圾回收机制-触发时机---------------------------------------


# 自动回收,默认时开启的
#
# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())

# gc.enable()

# print(gc.isenabled())

# print(gc.get_threshold())
# gc.set_threshold(1000, 15, 5)

# 手动回收
# import gc 
# import objgraph

# gc.disable()

# class Person:
#     pass
# class Dog:
#     pass

# p = Person()
# d = Dog()

# p.pet = d 
# d.master = p

# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))

# del p 
# del d

# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))

# # 手动回收
# gc.collect()

# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))


# -----------------------------------循环引用-细节问题(版本兼容方案)---------------------------------------
# 循环引用中有一环是弱引用的情况下使用计数器回收即可，不需要使用gc.collect垃圾回收
import objgraph
import gc
import weakref

class Person:
    # py2中如果实现了del方法，那么在执行del 这个实例时不会执行该自定义函数
    def __del__(self):       
        print("p对象被回收了")
class Dog:
    def __del__(self):
        print("d对象被回收了")

p = Person()
d = Dog()

p.pet = d
# 弱引用使用方式一:
p.pets = weakref.WeakValueDictionary({"dog":d})
# d.master = p

# pet属于不可达对象；
# weakref.ref(p)属于弱引用

# 弱引用使用方式二:
d.master = weakref.ref(p)
# 以下方法同理
# d.master = None

del p
del d 

print(objgraph.count('Person'))
print(objgraph.count('Dog'))
# gc.collect()


# print(objgraph.count('Person'))
# print(objgraph.count('Dog'))