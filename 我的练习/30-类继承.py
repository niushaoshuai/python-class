#-*- coding:utf-8 -*-
import inspect
### 类的继承顺序
#在py3都是新式类，是按广度的顺序来继承的，默认最后一个基类会继承object类
#在py2是经典类，是按深度的顺序来继承的
# py2 和 py3只在类的多继承重叠时有区别

# class C:
#     age = 13
#     pass
# class B(C):
#     age = 12
#     pass
# class A(B):
#     pass 
# p = A()
# print(p.age)
# print(inspect.getmro(A))
#py2 # (<class __main__.A at 0x7fb2a3a758d8>, <class __main__.B at 0x7fb2a3a75870>, <class __main__.C at 0x7fb2a3a75808>)
#py3 # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)

# class F:
#     pass
# class E(F):
#     pass
# class D(F):
#     pass
# class C(E):
#     age = 13
#     pass
# class B(D):
#     age = 12
#     pass
# class A(B,C):
#     pass 
# p = A()
# print(p.age)
# print(inspect.getmro(A))
# py2 # (<class __main__.A at 0x7fe916b5ba10>, <class __main__.B at 0x7fe916b5b9a8>, <class __main__.D at 0x7fe916b5b8d8>, <class __main__.F at 0x7fe916b5b808>, <class __main__.C at 0x7fe916b5b940>, <class __main__.E at 0x7fe916b5b870>)
# py3 # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>)

# class E:
#     pass
# class D:
#     pass
# class C(E):
#     age = 13
#     pass
# class B(D):
#     age = 12
#     pass
# class A(B,C):
#     pass 
# p = A()
# print(p.age)
# print(inspect.getmro(A))

# py2 # (<class __main__.A at 0x7faa2584d9a8>, <class __main__.B at 0x7faa2584d940>, <class __main__.D at 0x7faa2584d870>, <class __main__.C at 0x7faa2584d8d8>, <class __main__.E at 0x7faa2584d808>)
# py3 # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)

# py2 经典类深度优先，从左往右 。经典类广度优先（到共父节点时从左到右），从左到右

# C3算法两个公式
# 	L(object) = [object]
# 	L(子类(父类1, 父类2)) = [子类] + merge(L(父类1), L(父类2) , [父类1, 父类2])
# 注意
# 	+ 代表合并列表
# 	merge算法
# 		1. 第一个列表的第一个元素
# 			是后续列表的第一个元素且两个列表中间的列表中不存在该元素
# 			或者
# 			后续列表中没有再次出现
# 			则将这个元素合并到最终的解析列表中并从当前操作的所有列表中删除
# 		2. 如果不符合，则跳过此元素，查找下一个列表的第一个元素，重复1的判断规则
# 		3. 如果最终无法把所有元素归并到解析列表, 则报错

# class D(object):
#     # L(D(object)) = [D] + merge(L(object),[object])
#     #              = [D] + merge([object],[object])
#     #              = [D,object] + merge([],[])
#     #              = [D,object]
#     pass

# class C(D):
#     # L(C(D))  = [C] + merge(L(D),[D])
#     #          = [C] + merge([D,object],[D])
#     #          = [C,D] + merge([object],[])
#     #          = [C,D,object] + merge([],[])
#     #          = [C,D,object]
#     pass

# class B(D):
#     # L(B(D)) = [B,D,object]
#     pass

# class A(B,C):
#     # L(A(B,C)) = [A] + merge(L(B),L(C),[B,C])
#     #           = [A] + merge([B,D,object],[C,D,object],[B,C])
#     #           = [A,B] + merge([D,object],[C,D,object],[C])
#     #           = [A,B,C] + merge([D,object],[D,object],[])
#     #           = [A,B,C,D] + merge([object],[object],[])
#     #           = [A,B,C,D,object] + merge([],[],[])
#     #           = [A,B,C,D,object]
#     pass

# print(inspect.getmro(A))
# # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <type 'object'>)


# class F(object):
#     L(F(object)) = [F] + merge(L(object),[object])
#                  = [F] + merge([object],[object])
#                  = [F,object] + merge([],[])
#                  = [F,object]
#     pass

# class E(F):
#     L(E(F)) = [E] + merge(L(F),[F])
#             = [E] + merge([F,object],[F])
#             = [E,F,object] + merge([],[])
#             = [E,F,object]
#     pass

# class D(F):
#     L(D(F)) = [D,F,object]
#     pass

# class C(E):
#     L(C(E)) = [C] + merge(L(E),[E])
#             = [C] + merge([E,F,object],[E])
#             = [C,E] + merge([F,object],[])
#             = [C,E,F] + merge([object],[])
#             = [C,E,F,object] + merge([],[])
#             = [C,E,F,object]
#     pass

# class B(D):
#     L(B(D)) = [B] + merge(L(D),[D])
#             = [B] + merge([D,F,object],[D])
#             = [B,D] + merge([F,object],[])
#             = [B,D,F] + merge([object],[])
#             = [B,D,F,object] + merge([],[])
#             = [B,D,F,object]
#     pass

# class A(B,C):
#     L(A(B,C)) = [A] + merge(L(B),L(C),[B,C])
#               = [A] + merge([B,D,F,object],[C,E,F,object],[B,C])
#               = [A,B] + merge([D,F,object],[C,E,F,object],[C])
#               = [A,B,D] + merge([F,object],[C,E,F,object],[C])
#               = [A,B,D,C] + merge([F,object],[E,F,object],[])
#               = [A,B,D,C,E] + merge([F,object],[F,object],[])
#               = [A,B,D,C,E,F] + merge([object],[object],[])
#               = [A,B,D,C,E,F,object] + merge([],[],[])
#               = [A,B,D,C,E,F,object]

#     pass

# class D(object):
#     pass
# # L(D) = [D] + merge(L[object],[object])
# # L(D) = [D] + merge([object],[object])
# # L(D) = [D,object] + merge([],[])
# # L(D) = [D,object] 

# class C(D):
#     pass
# # L(C) = [C] + merge(L[D],[D])
# # L(C) = [C] + merge([D,object],[D])
# # L(C) = [C,D] + merge([object],[])
# # L(C) = [C,D,object] + merge([],[])
# # L(C) = [C,D,object]
# class B(C):
#     pass
# # L(B) = [B] + merge(L[C],[C])
# # L(B) = [B] + merge([C,D,object],[C])
# # L(B) = [B,C] + merge([D,object],[])
# # L(B) = [B,C,D] + merge([object],[])
# # L(B) = [B,C,D,object] + merge([],[])
# # L(B) = [B,C,D,object]

# class A(B,C):
#     pass
# # L(A) = [A] + merge(L[B],L[C],[B,C])
# # L(A) = [A] + merge([B,C,D,object],[C,D,object],[B,C])
# # L(A) = [A] + merge([B,C,D,object],[C,D,object],[B,C])
# # L(A) = [A,B] + merge([C,D,object],[C,D,object],[C])
# # L(A) = [A,B,C] + merge([D,object],[D,object],[])
# # L(A) = [A,B,C,D] + merge([object],[object],[])
# # L(A) = [A,B,C,D,object] + merge([],[],[])
# # L(A) = [A,B,C,D,object]

# ------------------------继承-资源的访问顺序-2.3-2.7 C3算法识别问题继承 ，如下代码会报错：order (MRO) for bases C, B-------------------------------------

class D(object):
    pass
# L(D) = [D,object] 

class B(D):
    pass
# L(B) = [B,D,object]

class C(B):
    pass
# L(C) = [C] + merge(L(B),[B])
# L(C) = [C] + merge([B,D,object],[B])
# L(C) = [C,B] + merge([D,object],[])
# L(C) = [C,B,D] + merge([object],[])
# L(C) = [C,B,D,object] + merge([],[])
# L(C) = [C,B,D,object]


class A(B,C):
    pass
# L(A) = [A] + merge(L(B),L(C),[B,C])
# L(A) = [A] + merge([B,D,object],[C,B,D,object],[B,C])

print(inspect.getmro(A))
