#作用域  变量生效的区域

from calendar import c
from threading import local


def fn():
    a=10
    b=20
    print(a)
#locals()获取当前作用域的命名空间
    print(locals())
    scope = locals()
    print(scope['b'])
#可以这样获取scope内的参数值


fn()
#函数内部定义的变量作用域在内部 函数作用域
#函数外部定义的作用域 全局


print("全局作用域"+str(locals()))

#globals() 可以在任意位置获取全局命名空间