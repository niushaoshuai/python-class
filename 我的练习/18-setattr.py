class Person(object):
    # 通过 “实例.属性=值” 给一个实例增加一个属性时 ，会自动调用这个方法
    # 在这个方法内部才会把属性、值追加到__dict__中
    def __setattr__(self,key,value):
        print(key,value)
        if key == "age" and key in self.__dict__.keys():
            print("只读属性，不允许做赋值操作")
        else:
            # 执行注释的这个方法会导致死循环
            # self.key = value
            self.__dict__[key] = value
    

p1 = Person()
p1.age = 18

print(p1.age)

p1.age = 999
print(p1.age)
