class Base:
    def beat(self):
        print("动物在打架")

class ShenxianBase(Base):
    # def beat(self):
    #     print("始祖在打架")
        pass

class Shenxian(ShenxianBase):
    def liandan(self):
        print("神仙会炼丹")
    # def beat(self):
    #     print("神仙在打架")



class MonkeyBase(Base):
    def beat(self):
        print("猿猴在打架")
    pass

class Monkey(MonkeyBase):
    def eattao(self):
        print("猴子会吃桃")
    def beat(self):
        print("猴子在打架")

# 从左到右继承
# 深度优先（一条分支走）
# 分支没有，再换另一分支
'''
class A: #经典类
    pass

class B(object): #新式类
    pass

在py2中，经典类采用的是深度优先查找，新式类采用的是广度优先
在py3中，无论经典类还是新式类都是按照广度优先查找(是在多分支有共同的原始base类时有效)
'''
class MonkeyKing(Shenxian,Monkey):
    def play_kkp(self):
        print("刷金箍棒")
    
mk1=MonkeyKing()
mk1.play_kkp()
mk1.beat()