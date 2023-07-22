class CreateFactory(object):
    def __init__(self,type):
        self.type = type

    # 使创建出来的实例具备可被调用的功能
    # 结合call方法，以类的方式实现了偏函数的功能
    def __call__(self,color):
        print("创建了%s,颜色是%s"%(self.type,color))

p1 = CreateFactory("pen")
p1("黑色")
p1("白色")
p1("黄色")
