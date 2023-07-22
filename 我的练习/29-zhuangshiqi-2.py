import logging

def use_logging(func):
    # 接收传参的位置，将来要用wrapper函数替换func函数
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@use_logging
def foo(*args, **kwargs):
    print("i am foo",args,kwargs)

# foo = use_logging(foo)

foo("hello",a="aaa",b="bbb")