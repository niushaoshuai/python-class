# 跨模块中_a不可访问
# import privateM15
# print(privateM15._a)

# 跨模块中_a不可访问，只有当被导入的模块中使用__all__ 指定相关私有变量时才可以
from privateM15 import *
print(_a)