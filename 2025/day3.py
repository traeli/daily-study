#.1.集合
# 基本格式：集合名={}      特点：具有唯一性和无序性
s1={}                 #这是字典
print(type(s1))
s1=set()              #空集合这样定义
print(type(s1))

# (1)添加元素
# add() ：添加的是一个整体(一个元素)
# update() ：添加的必须是可迭代对象，拆开并放于集合中
s1={1,2,3,4}
s1.add(5)         #也可以添加元组
print(s1)
s1.update('hell569')
print(s1)
print('==============')

# (2)删除元素
# remove() ：选择要删除的元素，有就删除，没就会报错
# discard() ：选择要删除的元素，有就删除，没不会报错
# pop : 默认删除哈希表排序后的第一个元素,数字则删除第一个
s2={1,2,3,4,5}
s2.remove(5)
print(s2)
s2.discard(6)
print(s2)
s2.pop()
print(s2)
# (3)交集和并集
# 交集：& 并集：|

#.2.类型转换
# (1) int()：转换成一个整数
str="+10"           #字符串中有数字或者正负号以外的字符就会报错
print(int(str))
# (2)float()：转换成一个小数
# (3)str()： 转换成字符串类型，任何类型都可以转字符串
# (4)eval()：用来执行一个字符串表达式，并返回结果
print(eval('10+10'))
# 注意：也可以实现list,dic,tuple和str之间的转换
s1="[1,2,3,5]"
s2=eval(s1)
print(s2,type(s2))
s1="1,2,3,4"
s2=eval(s1)
print(s2,type(s2))
# (5) list()：将可迭代对象转换成列表
#             可迭代对象:str,tuple,dic,set

#.3.深浅拷贝
# (1)赋值: 等于完全共享资源，一个值的改变会被另一个值共享
li=[1,2,3,4]
li1=li
print(li)
print(li1)
li.append(5)
print(li)
print(li1)

# (2)浅拷贝(数据半共享)：会创建新的对象，会拷贝第一层数据，嵌套层的指向原来的内存地址
import copy   #导入模块
# 查看内存地址  id()
li=[1,2,3,4,[5,6,7]]
li1=copy.copy(li)
print(li)
print(li1)
li.append(8)
print(li)
print(li1)
li[4].append(8)
print(li)
print(li1)
print(id(li),id(li1),id(li[4]),id(li1[4]))

print('==========================')
# (3)深拷贝(数据完全不共享):外层的对象和内部的元素全拷贝一遍
import copy #导入模块
li=[1,2,3,4,[5,6,7]]
li1=copy.deepcopy(li)
print(id(li),id(li1),id(li[4]),id(li1[4]))

#.4.可变对象
# 含义： 变量的值可以改变，但是内存地址不会改变
# 常见的可变对象:list set dic
#.5.不可变对象
# 含义：变量的值不允许被修改，修改了就会重新分配内存地址
# 常见类型：int  float  str  bool complex  tuple

#.6.函数
#(1) 格式
#  def 函数名(形参):
#      函数体
#      return(可有可无，在这函数就结束了)
def fun(b,a=8):
    print(a,b)
fun(100)
# (2)参数
# 1.必备参数(位置参数)
#  注意：传递参数的顺序及个数必须一致
def funa(a,b):
    return  a+b
print(funa(1,2))
# 2.默认参数
#  含义：为函数提供默认值
#  注意：所有的位置参数必须在默认参数之前
def funb(a=8):
    print(a)
funb(100)       #有默认值，如果传了值就根据传的值运行代码
# 3.可变参数
# 含义：函数传入的值的数量是可以改变的，也可以不传
#  格式：def 函数命(*args):
def func(*args):
    print(type(args))
func(1,2)           #是以元组的形式传入
# 4.关键字参数
# 格式：def 函数命(**kwargs):
def func2(**kwargs):
    print(kwargs)
func2(name="lizhiyan",age=18)     #以字典的形式传
# (3)作用域
#  分为全局变量和局部变量






