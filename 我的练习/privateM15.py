class Animal:
    _x = 10
    def test(self):
        print(Animal._x)
        print(self._x)

class Dog(Animal):
    def test2(self):
        print(Dog._x)
        print(self._x)

# 受保护参数在类、子类中都能被访问到
#          在模块的其他地方访问，提示不规范


# a = Animal()
# b = Dog()

# print(Animal._x)
# print(Dog._x)
# a.test()
# b.test2()

_a = "666"

# 允许模块导入时将私有变量导入过去
__all__ = ["_a"]