def a(func):
    def inner():
        func()
        print("a")

    return inner


def b(func):
    def inner():
        func()
        print("b")
    return inner

def c(func):
    def inner():
        func()
        print("c")
    return inner

# 执行顺序由下而上的
@a
@b
@c
def foo():
    print("装饰器顺序：")



foo()