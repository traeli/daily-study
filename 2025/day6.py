#.1.面向对象
# (1)类是一系列具有相同属性和行为的事物的统称，不是真是存在的
#    对象是类的具体表现，是类创造出来的具体存在的真实的事物，面向对象的核心
#  先有类，再有对象
# (2)类的三要素
#  类名    属性：对象特征的描述，用来说明对象是什么   方法：能做什么
# (3)类定义：     class 类名:
#                         代码块
class people:
    name='李志研'
# 访问类里面的属性 类名.属性
print(people.name)
# 添加属性
people.age=20
print(people.age)
# (4)创建对象：也是实例化对象过程
# 基本格式：对象名=类名()
people1=people()
# (5)实例方法和实例属性
#  1.实例方法：由对象调用，至少有一个self参数，执行实例方法的时候，自动将调用该方法的对象赋值给self
class people1:
    name = '李志研'
    def cando(self):       #self：是类中的实例方法必备的，是对象本身
        print("我想吃达美乐")
Peopel1=people1()
Peopel1.cando()
# 2.实例属性         格式：self.属性名
# 实例属性和类属性的取别：类属性属于类，是公共的，实例属性是属于对象的，私有的
class people2:
    name = '李志研'
    def cando(self):
        print(f'{people2.name}想吃达美乐',self.age)
People2=people2()
People2.age=20
People2.cando()
# (6)构造函数 __init__()
# 作用：用来做属性初始化或赋值      注意：在实例化对象的时候，会被自动调用
class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def play(self):
        print(f'{self.name}喜欢打三角洲')
    def introduce(self):
        print(f'{self.name}是{self.age}岁,身高{self.height}cm')
pe=Person('李志研',20,180)
pe.play()
pe.introduce()
# (7)析构函数 ：__del__()
# 作用：删除对象的时候，解释器会默认调用__del__()
class Person1:
    def __init__(self):
        print('这是__init__()函数')
    def __del__(self):
        print('这是__del__()函数')
pe1=Person1()
del pe1
print("这是最后一行")        #正常运行时，不会调用__del__(),对象执行结束后，会自动调用__del__()
# (8)封装
# 1.私有属性(私有权限)，只允许在类的内部进行使用，无法通过对象访问,不能被继承，子类也无法使用
# 格式：在属性名或者方法前加__
# 2.隐藏属性，格式：_类名或方法，可以在类外部直接使用
class Person2:
    name='李志研'
    _height=180
    __age=20
    def introduce(self):
        print(f'我的年龄是{self.__age}')
pe2=Person2()
print(Person2._height)
print(pe2._height)
pe2.introduce()
# 调用隐藏属性方式一：实际上是将属性名改为了_类名__属性名
print(pe2._Person2__age)
# 方式二：通过类里面的实例方法调用

# (9)继承
# 1.格式：class 类名(父类)：
#           代码块
class Person3:
    def eat(self):
        print("会吃饭")
    def play(self):
        print("我贪玩")
class Girl(Person3):
    pass                  #不写代码的时候用，防止报错
girl=Girl()
# 2.继承具有传递性
# 3.方法重写：子类定义与父类相同的方法
# 第一种：覆盖
class Father:
    def money(self ):
        print("有一百万遗产")
class Son(Father):
    def money(self ):
        print("有一千万遗产")
son=Son()
son.money()
# 第二种方式：对父类的方法进行扩展
# 调用父类的方法：1. 父类名.方法名(self)          2.super().方法名()
class Father1:
    def money(self ):
        print("有2百万遗产")
class Son1(Father1):
    def money(self ):
        Father1.money(self)
        super().money()
        print("我买劳斯莱斯")
son1=Son1()
son1.money()

# (10)新式类写法
# class A:        经典类：不由任意内置类派生出来的类
class Animal:
    def eat(self):
        print("chi")
class Dog(Animal):
    def play(self):
        print('wan')       #派生类：有不同于父类的属性和方法

# (11)多继承
class Father2:
    def money(self ):
        print("有一亿财产需要被继承")
class Mother2:
    def money(self ):
        print("有123000财产需要被继承")
    def apprenance(self):
        print('需要继承颜值')
class Son2(Father2,Mother2):
    pass
son2=Son2()
son2.apprenance()
son2.money()                   #调用继承最近的，也就是Father2
# 方法搜索顺序:
# python中内置属性：__mor__查看
print(Son2.__mro__)











