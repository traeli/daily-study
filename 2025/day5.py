#.1.内置全局变量
# 语法：if __name__="__main__"
# 作用：将要导入的函数中，有些不想展示的东西，隐藏起来
import pytest1
pytest1.fun1()
#.2.包
# (1)与普通文件夹的区别：包含有_init_.py
#import pack01          #导包时，会自动执行_init_.py里面的代码
#from pack01 import register
#register()
#register.fun1()
# 不建议在_init_.py中写过多代码

# (2)__all__
# 作用：本质上是一个列表，列表里面的元素代表要导入的模块
from pack01 import *
register.fun1()

#.3.递归函数
def add(n):
    if n==1or n==2:
        return 1
    return add(n-1)+add(n-2)     #add(3)=add(2)+add(1)
print(add(6))

#.4.闭包
# (1)条件：嵌套函数
#         内层函数使用外层函数的局部变量
#         外层函数返回内层函数的的函数名
def outer(m):
    a=10
    def inner():
        print('两数之和=',a+m)
    return inner
outer(2)()           #调用方式一
#ou=outer()           #调用方式二
#ou()
# (2)每次开启内函数都在使用同一份闭包变量
def outer1(m):
    print('这是outer1()中函数的值：',m)
    def inner1(n):
        print('这是inner1()中函数的值:',n)
        return m+n
    return inner1
ou1=outer1(10)
print(ou1(10))
print(ou1(30))
print(ou1(50))

#.5.装饰器
# (1)本质上是一个闭包函数
#  特点：不改变原程序或函数的代码，不改变函数或程序调用的方法
# (2)标准版装饰器
def send():
    print("发送消息")
def outer2(fn):
    def inner2():
        print('登录')
        fn()
    return  inner2
outer2(send)()
# (3)语法糖形式：在被装饰的函数前加上 @外层函数名称
def outer3(fn):
    def inner3():
        print('登录')
        fn()
    return inner3
@outer3
def send1():
    print('你是哈皮')
send1()
# (4)被传入的函数有参数
def outer4(fn):
    def inner4(*args,**kwargs):
        print(args)
        print(kwargs)
        fn(*args,**kwargs)
    return inner4
@outer4
def send2(*args,**kwargs):
    print('这是被装饰的函数')
send2('halo',name='李志研')

def outer5(fn):
    def inner5(*args,**kwargs):
        print(args)
        print(kwargs)
        fn(*args,**kwargs)
    return inner5
def send3(*args,**kwargs):
    print("这是被装饰的函数")
outer5(send3)(123,age=18)

print('========================')
# (5)多个装饰器
# 装饰过程：离函数最近的装饰器先装饰，然后外面的装饰器在装饰，由内到外
def outerone(fn):
    def innerone():
        return '第一个装饰器的运行：'+fn()+'!!!'
    return innerone
def outertwo(fn):
    def innertwo():
        return'第二个装饰器的运行:'+fn()+'???'
    return innertwo
@outerone
@outertwo
def send4():
    return '今天晚上继续学python'
print(send4())


