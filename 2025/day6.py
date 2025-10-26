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
    def __init__(self,name,age,height):             #实例属性
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

# (12)多态
# 要有继承和方法重写
class Animal1:
    def eat(self):
        print("我会感饭")
class Dog1(Animal1):
    def eat(self):
        print('狗吃狗粮')
class Cat1(Animal1):
    def eat(self):
        print('猫吃猫粮')
def test1(obj):              #定义一个统一的接口，一个接口多种实现
    obj.eat()
dog1=Dog1()
test1(dog1)

# (13)静态方法
# 使用@staticmethod修饰
class AA():
    @staticmethod
    def play():
        print('hhhhhhh')
#既可以使用对象访问，也可以用类访问
AA.play()
aa=AA()
aa.play()
# (14)类方法
# 基本格式:class 类名：
#              @classmethod
#              def 方法名(cls,形参)
#                   代码块
class A():
    @classmethod
    def play(cls):
        print('hhhhhhh11')
A.play()
#当方法中需要使用到类属性(如：访问私有类属性)，需定义类方法
# 类方法一般配合类属性使用

# (15)实例方法，静态方法，类方法总结
# 实例方法：方法内部可以访问实例属性和类属性，通过类名.属性名访问类属性
# 静态方法：方法内部不需要访问类属性和实例属性
# 类方法：方法内部只需要访问类属性，不可以访问实例属性
class Person4():
    name='李志研'   #类属性
    def __init__(self):
        self.age=20     # 实例属性
    def introduce(self):     #实例方法
        print(f'我是{Person4.name},{self.age}大了')
    @staticmethod
    def play():
        print('我打三角洲')
        print(Person4.name)    # 可以访问，但没意义
    @classmethod
    def hobby(cls):
        print(Person4.name)   #不可以访问实例方法
Pe4=Person4()
Pe4.introduce()
Person4.play()
Person4.hobby()

# (16)__new__()和__init__()
# __new__()：object基类中提供的内置的静态方法
# 作用：1.在内存中为对象分配空间  2.返回对象的引用
class Person5():
    def __init__(self):
        print("这是__int__(self)方法")
    def __new__(cls):           #cla代表类本身
        print('这是__new__(cls)方法')
        print(cls)
        return super().__new__(cls)     #方法重写，__new__()里面是保存的对象的引用
    #注意：重写__new__()，一定要return super().__new__(cls)，不然没返回对象的引用就不能实例化对象
Pe5=Person5()
print('Pe5:',Pe5)
#总结：(1)__new__()是创建对象，__init__()是初始化对象
#     (2)没__new__()就没__init__()

# (17)单例类
# 相当于一个特殊的类，这个类只存在一个对象
# 1.方式
# (1)通过@classmethod   (2)通过装饰器实现  (3)通过重写__new__()(重点) (4)通过导入模块实现
# 方式三：通过重写__new__()实现
# 设计模式：
# 第一步：定义一个类属性，初始值为None，用来记录单例类对象的引用
# 第二步：重写__new__()方法
# 第三步：判断
# 第四步：返回引用
class Singpo():
    obj=None
    def __new__(cls, *args, **kwargs):
        if Singpo.obj==None:
            Singpo.obj=object.__new__(cls)
        return Singpo.obj
S1=Singpo()
print(S1)
S2=Singpo()
print(S2)

# (18)魔法方法：在python中，__什么__()都是，魔法方法
# __doc__()：类的描述信息
class Doc1():
    '''类的描述信息'''      #只能用三引号
    pass
print(Doc1.__doc__)
doc1=Doc1()
# __module__()：表示当前操作所在的模块
# __class__()：表示当前操作所在的类
print(doc1.__module__)
print(doc1.__class__)

# __str__()：必须返回一个字符串
class Str1():
    def __str__(self):
        return '123456'
str1=Str1()
print(str1.__str__())

# __call__()：使一个实例对象是一个可调用对象，就像函数那样可以调用
# 可调用对象：函数、内置函数、类都是，凡是把一队()应用到某个对象身上都是可调用对象
# 判断可调用对象：callable()
print(callable(str1))
class Str2():
    def __call__(self):
        pass
str2=Str2()
print(callable(str2))














