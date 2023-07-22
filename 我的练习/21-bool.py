class Person:
    def __init__(self,age):
        self.age = age
    # 控制实例对象的布尔值
    def __bool__(self):
        if self.age >= 18:
            return True
        else:
            return  False

p1 = Person(16)

if p1:
    print("成年人")
else:
    print("未成年")