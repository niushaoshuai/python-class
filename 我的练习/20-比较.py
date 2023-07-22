import functools

# 这个装饰器可以通过一个比较方法推导除其他的比较方法
# 如果没有ge或者le方法，它会去gt,eq 或者lt、eq中去找
## 紧接上面，如果gt 返回true，则不会再去eq方法中执行逻辑
@functools.total_ordering
class Person:
    def __init__(self,age,height):
        self.age = age
        self.height = height

    def __eq__(self, other):
        print("eq")
        return self.age == other.age
    # def __ne__(self, other):
    #     return  self.height != other.height
    def __gt__(self, other):
        print("gt")
        return self.height > other.height
    # def __ge__(self, other):
    #     print("ge")
    #     return self.height >= other.height
    # def __lt__(self, other):
    #     return self.age < other.age
    # def __le__(self, other):
        # return self.age <= other.age

p1 = Person(18,195)
p2 = Person(18,190)

# print(p1 == p2)
# print(p1 != p2)
# print(p1 > p2)
print(p1 >= p2)
# print(p1 < p2)
# print(p1 <= p2)

print(Person.__dict__)