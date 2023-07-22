
# 函数装饰器
# def check(func):
#     # 闭包
#     def inner():
#         print("登录验证")
#         # 执行函数
#         func()
#     return  inner

# 类装饰器
class check:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("登录验证")
        return self.func()

# 装饰器方式1
@check
def fashuoshuo():
    print("发说说")
# 装饰器方式2
# fashuoshuo = check(fashuoshuo)

fashuoshuo()