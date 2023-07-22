# _*_ encoding:utf-8 _*_

# 计算器, 实现一些基本的操作, 加减乘除运算, 以及打印结果操作

# ------------------------------------代码1--------------------------------------
# def jia(n1, n2):
#     return n1 + n2

# def jian(n1, n2):
#     return n1 - n2

# def cheng(n1, n2):
#     return n1 * n2

# # res = jia(2, 4)
# # res2 = cheng(5, 7)
# # print(res)
# # print(res2)
# # (2 + 6 - 4) * 5

# r1 = jia(2, 6)
# r2 = jian(r1, 4)
# r3 = cheng(r2, 5)
# print(r3)


# ------------------------------------代码2--------------------------------------
# count = 0
# def first_value(v):
#     global count
#     count = v
# def jia(n):
#     global count
#     count += n 

# def jian(n):
#     global count
#     count -= n

# def cheng(n):
#     global count
#     count *= n

# first_value(2)
# jia(6)
# jian(4)
# cheng(5)
# print(count)


# # ------------------------------------代码3--------------------------------------
# class Caculator:
#     __count = 0
#     @classmethod
#     def first_value(cls,v):
#         cls.__count = v

#     @classmethod
#     def jia(cls,n):
#         cls.__count += n 

#     @classmethod
#     def jian(cls,n):
#         cls.__count -= n

#     @classmethod
#     def cheng(cls,n):
#         cls.__count *= n

#     @classmethod
#     def result(cls):
#         return cls.__count

# Caculator.first_value(2)
# # Caculator.__count = 22
# Caculator.jia(6)
# Caculator.jian(4)
# Caculator.cheng(5)
# print(Caculator.result())


# # ------------------------------------代码5--------------------------------------
# class Caculator:
#     def check_num(self,n):
#         if not isinstance(n,int):
#             raise TypeError("当前应该数值应为一个整形")
#     def __init__(self,count):
#         self.check_num(count)
#         self.count = count

#     def jia(self,n):
#         self.check_num(n)
#         self.count += n 

#     def jian(self,n):
#         self.check_num(n)
#         self.count -= n

#     def cheng(self,n):
#         self.check_num(n)
#         self.count *= n

#     def result(self):
#         return self.count

# p1 = Caculator(2)
# p1.jia(6)
# p1.jian("a")
# p1.cheng(5)
# print(p1.result())

# p2 = Caculator(2)
# p2.jia(6)
# p2.jian(4)
# p2.cheng(5)
# print(p2.result())


# # ------------------------------------代码6--------------------------------------
# class Caculator:
#     def check_num(self,n):
#         if not isinstance(n,int):
#             raise TypeError("当前应该数值应为一个整形")
#     def __init__(self,count):
#         self.check_num(count)
#         self.count = count

#     def jia(self,n):
#         self.check_num(n)
#         self.count += n 

#     def jian(self,n):
#         self.check_num(n)
#         self.count -= n

#     def cheng(self,n):
#         self.check_num(n)
#         self.count *= n

#     def result(self):
#         return self.count

# p1 = Caculator(2)
# p1.jia(6)
# p1.jian("a")
# p1.cheng(5)
# print(p1.result())

# p2 = Caculator(2)
# p2.jia(6)
# p2.jian(4)
# p2.cheng(5)
# print(p2.result())


# # ------------------------------------代码7--------------------------------------
# class Caculator:
#     def __check_num(func):
#         def inner(self,n):
#             if not isinstance(n,int):
#                 raise TypeError("该值应为一个整形")
#             return func(self,n)
#         return inner

#     @__check_num
#     def __init__(self,count):
#         self.count = count
#     @__check_num
#     def jia(self,n):
#         self.count += n 
#     @__check_num
#     def jian(self,n):
#         self.count -= n
#     @__check_num
#     def cheng(self,n):
#         self.count *= n

#     def result(self):
#         return self.count

# p1 = Caculator(2)
# p1.jia(6)
# p1.jian(4)
# p1.cheng(5)
# print(p1.result())

# p2 = Caculator(2)
# p2.jia(6)
# p2.jian(4)
# p2.cheng(5)
# print(p2.result())

# ------------------------------------代码8--------------------------------------
class Caculator:
    # 装饰器方式一、不传参的情况
    def __check_num(func):
        def inner(self,n):
            if not isinstance(n,int):
                raise TypeError("该值应为一个整形")
            return func(self,n)
        return inner

    # 装饰器方式二、传参的情况
    def say_word(word=""):
        def say(func):
            def inner(self,count):
                # print(func(self,count))
                print(word,count,"=",func(self,count))
                return func(self,count)
            return inner
        return say
    
    @say_word()
    @__check_num
    def __init__(self,count):
        self.count = count
        # return self.count
    
    @say_word("加")
    @__check_num
    def jia(self,n):
        self.count += n 
        v = self.count
        return v
        

    @say_word("减")
    @__check_num
    def jian(self,n):
        self.count -= n
        v = self.count
        return v
    
    @say_word("乘")
    @__check_num
    def cheng(self,n):
        self.count *= n
        v = self.count
        return v

    def result(self):
        return self.count

p1 = Caculator(2)
p1.jia(6)
p1.jian(4)
p1.cheng(5)
print(p1.result())
