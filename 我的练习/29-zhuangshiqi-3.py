import logging

def decorator(level=""):
    def use_logging(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            else:
                logging.error("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return use_logging

# @decorator(level="warn1") 相当于 @use_logging装饰器 并把参数level传递到装饰器环境中
@decorator(level="warn1")  
def foo(*args, **kwargs):
    print("i am foo",args,kwargs)


foo("hello",a="aaa",b="bbb")