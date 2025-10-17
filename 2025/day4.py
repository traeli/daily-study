#.1.global关键字                格式：global 变量名
# 将局部变量申明为全局变量
#.2.nonlocal关键字
# 用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数先进行申明，内部函数进行nonlocal申明
# 只能对上一层函数进行修改
#.3.匿名函数
# 格式：函数命=lambda 形参:返回值
add=lambda a,b:a+b
print(add(1,2))
#.4.内置函数
# (1)查看内置函数
import builtins
print(dir(builtins))
# 大写字母开头一般是内置常量名，小写字母开头一般是内置函数名
# (2) abs()：返回绝对值
print(abs(-2))
# (3) sum()：求和
print(sum([1,2,3]))      #里面必须是可迭代对象，字符串除外
# (4) min()：求最小值         max()：求最大值
print(min(1,2,9))
print(max(55,2))
print(min(-5,2,key=abs))         #求绝对值的最小值
# (5) zip()：将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
li=[1,2,3]
li1=['a','b','c']
#方式一：
for i in zip(li,li1):
    print(i)
#方式二：
print(list(zip(li,li1)))        #转换成列表打印
# (6)map()：将可迭代对象中的元素一一进行映射，分别去执行
# map(func,iterl)      func:函数名 iterl:可迭代对象
funa=lambda x:x*5
li=[1,2,3]
ma=map(funa,li)       #map()：返回的是可迭代对象，只能用一次 用完就没了
#两种方式
for i in ma:
    print(i)
print(list(ma))
# (7) reduce()：先把对象中两个元素取出，计算第一个值然后保存，然后这个值跟第三个元素计算
from functools import reduce    # 先导包
# reduce(function,sequence)    function--必须是两个参数的函数,sequence--可迭代对象
li=[1,2,3,4,5,6]
def func(a,b):
    return a+b
sum=reduce(func,li)
print(sum)
print(reduce(func,li))

#.5.拆包
# 将列表，元组，字典，集合中的元素取出来
tua=(1,2,3)
a,b,c=tua           #方式一
print(a,b,c)
a,*b=tua
print(a,b)          #方式二
#.6.异常
# (1) 格式： try:
#           可能出现异常的代码
#       except Exception(万能异常) as e:
#           出现异常的代码处理
#        else(可选):
#            未出现异常的代码处理
#       finally:
#           try执行后执行的语句
try:
    print(aaaa)
except Exception as e:
    print("出现错误")
    print(e)
else:
    print("没错")
finally:
    print('恭喜通过')
# (2) 异常传递： 在主函数中设置异常捕获机制，调用子函数
def fun1():
    return int(input("请输入一个整数:"))
def fun2():
    return 10/fun1()
try:
    print(fun2())
except Exception as e:
    print(e)
# (3)抛出异常 raise
# raise Exception("......")    ...：异常提示信息
def login():
    code=input("请输入密码:")
    if len(code)>=6:
        return '密码输入成功'
    else:
        raise Exception('密码长度不足6位')
try:              # 防止代码终止运行
    login()
except Exception as e:
    print(e)

#.7.模块
# 含义：一个py文件就是一个模块，导入一个模块本质上是运行一个文件
# (1)模块分类
# 1.内置模块 ：导入就可以用
# 2. 第三方模块(第三方库)
# 下载：cmd窗口输入 pip install 模块名
# 3.自定义模块

# (2)导入模块
# 方式一：import 模块名
import hhhh
print(hhhh.name)
hhhh.funa()
# 方式二：from 模块名 import 功能
# 方式三：from 模块名 import *     导入所有功能

# (3)给模块起别名
# import 模块名 as 别名
import hhhh as f
print(f.name)
f.funa()
# (4)给功能起别名
# from 模块名 import 功能 as 别名
from hhhh import funa as f1,name    #导入多个功能，用，隔开
f1()
print(name)



