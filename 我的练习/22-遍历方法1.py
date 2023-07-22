# class Person:
#     def __init__(self):
#         self.count = 0
#     def __getitem__(self, item):
#         print("item: "+str(item))
#         self.count += 1
#         # 通过一个条件抛出一个异常来终止循环
#         if self.count > 6 :
#             raise StopIteration("停止遍历")
#         return self.count
#     def __iter__(self):
#         # 比__getitem__的优先级高
#         # return iter([1,2,3])
#         ## 需要返回一个迭代器iter()，而迭代器需要next方法去访问
#         return self
#         pass

# p = Person()
#
# for i in p:
#     print(i)

# ### 举例,由此可见类中需要实现iter和next方法才能实现遍历 ###
# l = [1,2,3]
# # 获取l对象的迭代器
# x = iter(l)
# print(next(x))
# print(next(x))
# print(next(x))

# # 方式2
# class Person:
#     def __init__(self):
#         self.count = 0
#     # 把实例封装成一个迭代器
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.count += 1
#         # 通过一个条件抛出一个异常来终止循环
#         if self.count > 6 :
#             raise StopIteration("停止遍历")
#         return self.count
#
# p1 = Person()
#
# # 以下两种方式都可以去遍历，for方式访问会规避掉raise的异常
# # for i in p1:
# #     print(i)
#
# while True:
#     print(next(p1))

class Person:
    def __init__(self):
        self.count = 0
    # def __getitem__(self, item):
    #     self.count += 1
    #     # 通过一个条件抛出一个异常来终止循环
    #     if self.count > 6 :
    #         raise StopIteration("停止遍历")
    #     return self.count
    # 把实例封装成一个迭代器
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        # 通过一个条件抛出一个异常来终止循环
        if self.count > 6 :
            raise StopIteration("停止遍历")
        return self.count
    def __call__(self, *args, **kwargs):
        self.count += 1
        # 通过一个条件抛出一个异常来终止循环
        if self.count > 6:
            raise StopIteration("停止遍历")
        return self.count

p1 = Person()
# 以下正常，需要有next和iter方法
pt = iter(p1)
# 以下不在执行next方法，而会直接执行call方法，到4不会输出出来
pt = iter(p1,4)
print(pt is p1 )

for i in pt:
    print(i)

# import collections
# # 迭代器 ，需要实现两个方法 iter和next
# print(isinstance(p1, collections.Iterator))
# # 可迭代对象，只需要实现iter一个方法即可
# print(isinstance(p1, collections.Iterable))