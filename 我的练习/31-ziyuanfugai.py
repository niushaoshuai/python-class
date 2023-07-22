# _*_ encoding:utf-8 _*_
# ------------------------继承-资源的覆盖-------------------------------------
# class D:
#     d = 1
#     def testd(self):
#         print("testd")
    
# class C(D):
#     def __init__(self):
#         self.c = 2
#     @classmethod
#     def testc(cls):
#         print("testc")

# class B(D):
    
#     @staticmethod
#     def testb():
#         print("testb")

# class A(B,C):
#     pass

# a_obj = A()
# print(a_obj.d)
# print(a_obj.testd())
# print(a_obj.c)
# print(A.testc())
# print(a_obj.testb())

# ------------------------------继承-资源的累加-supper-------------------------------------
class D(object):
    def __init__(self):
        print("d")

class B(D):
    ### 实例属性
    def __init__(self):
        # D.__init__(self)
        super(B,self).__init__() # py2
        # super().__init__()  #py3
        print("b")

    ### 类方法
    @classmethod
    def testb(cls):
        print("testb")

    ### 静态方法
    @staticmethod
    def testbb():
        print("testbb")

class C(D):
    def __init__(self):
        # D.__init__(self)
        super(C,self).__init__() # py2
        # super().__init__() #py3
        print("c")

    @staticmethod
    def testc():
        print("testc")

    ### 实例方法
    def testcc(self):
        print("testcc")

class A(B, C):
    def __init__(self):
        # B.__init__(self)
        # C.__init__(self)
        super(A,self).__init__() # py2
        # super().__init__() #py3
        print("a")
    
    @classmethod
    def testa(cls):
        ### 继承类方法
        super(A,cls).testb() #py2
        # super().testb() # py3
        print("testa")

    @staticmethod
    def testaa():
        # 继承静态方法,super的两个参数都要使用类名
        # super(A,A).testb() # py2\py3
        print("testaa")

    def testaaa(self):
        ### 继承实例方法
        # super(A,self).testcc() # py2
        super().testcc()  #py3
        print("testaaa")



# A()
# A.testa()
# A().testaa()
A().testaaa()
