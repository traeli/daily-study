#.1.字符串运算符
#(1)+: 表示两个字符串相加  *n:表示字符串重复输出n便
str=input("请输入你的名字:")
print(str*2)
#(2)成员运算符
# in:如果包含，返回True  not in：如果不包含，返回False
print('i' in str)

#.2.索引
# 从左往右是从0开始，从右往左是从-1开始

#.3切片
# 格式：字符串名[下标值]
# [初始位置:末位置:步长] 注意：包前不包后，步长默认是1
print(str[1:6:2])

#.4.字符串常规操作
#(1)  find()和index() 格式一样
# 检查某个子字符串是否包含在字符串中，是，则返回下标，否，find()返回-1，index()会报错
# 格式：find(子字符串,开始下表,结束下标) 后面的可以省略
print(str.find('z'))
#(2)count() 格式和上面一样
# 返回子字符串出现的次数，没有出现返回0
#(3) startswich()：检测某个字符串是否以什么开头
#     endswich():检测某个字符串是否以什么结尾
# 格式 startswich或endswich(子字符串,初位置，末尾置)
#(4)isupper() ：检测字符串中是否都是大写
print("SEX".isupper())
#(5)replace() 替换
# replace(旧内容,新内容,替换次数)
st='Hello,python'
print(st.replace('o','ll'))
#(6)split()：指定分隔符来切字符串
print(st.split(','))   #['Hello', 'python'] 以列表的形式返回
print(st.split('o',2))
#(6) capitalize()：第一个字母大写，其他小写
str='hello World'
print(str.capitalize())
#(7)lower()：大写字母转为小写字母
#(8)upper()：小写字母转为大写字母

print('==============================')
#.5.列表
# 基本格式   列表名=[元素一,元素二]
# 里面的数据可以是不同类型的，是可迭代对象
li=[1,2,'a',5]
print(li)

#.6.列表的基本操作
# (1)添加
# append()  extend() insert()
li=[1,2,3,'abc',6]
li.append(7)
print(li)      #在末尾添加
li.extend('lizhiyan')
print(li)      #必须添加的是字符类型，将字符串一个个拆开，并添加在末尾
li.insert(1,'hello')
print(li)      #在指定位置插入
#(2)修改和查找
li=[1,2,3,4,5]
li[2]=999        #修改
print(li)
#查找 用in和not in 用法和字符串用法一样
#昵称输入，不能重复输入
name_list=['Hello','victory','hapi']
while True:
    name=input('请输入你要的昵称：')
    if name  in name_list:
        print(f'你输入的昵称{name}已经存在了')
    else:
        print(f'{name}就是你的昵称了')
        name_list.append(name)
        print(name_list)
        break
#index()和count()用法与字符串相同

#(3)删除元素
# del pop remove
li=['a','b','c','d','e']
#del li
print(li)    #删除列表
del li[2]
print(li)

li.pop()
print(li)          #默认删除最后一个元素 根据索引删除
print(li.pop(0))   #会返回删除的元素
print(li)

li.remove('b')      #根据元素删除
print(li)

#(4)排序
# sort：从小到大排序    reverse：倒序
li=[55,12,3,65,999,41]
li.sort()
print(li)
li.reverse()
print(li)

#(5)列表推导式
# 格式一：[表达式 for 变量 in 列表]         in后面还可以放可迭代对象，range()
li=[1,2,3,4,5]
[print(i) for i in li]
li=[]
for i in range(1,6):
    li.append(i)
print(li)
#格式二：[表达式 for 变量 in 列表 if 条件
li=[]
for i in range(1,11):
    if i%2==1:
        li.append(i)
print(li)
li=[]
[li.append(i) for i in range(1,11) if i%2==1]
print(li)

print('==================')
#.7.元组 tuple
# 基本格式： 元组名=()        注意：可以是不同的数据类型，只有一个元素时，后面要加,
li=(1,2,3)
print(type(li),li)

#应用场景 1.函数的参数和返回值，2.格式化输出后面的()本质上是一个元组

#.8.元组与列表的取别
# 元组只能查找，不支持增删改，而列表都可以
print(li.index(1))

#.9.字典
# 格式：字典名={键名1:值1，键名2:值2}
# 字典中的键具有唯一性，但是值可以重复
dic={'name1':"lizhiyan",'name2':'python'}
print(dic)

#.10.字典的操作
# (1)查找     方式一：字典名[键名]   方式二：字典名.get(键名)
dic={'name':'李志研','age':20}
print(dic['name'])
print(dic.get('age'))
print(dic.get('ag',0))      #键名不存在返回none,可以自己设定
#(2)修改：通过键名修改
dic['name']='halo'
print(dic)
# (3)添加
# 注意：键名不存在就是添加，存在就是修改
dic['height']=180
print(dic)
# (4)删除
# 1.del        方式一：del+变量名 表示删除整个键值对 方式二：del+变量名[键名]
#del dic
#print(dic)
del dic['age']
print(dic)
# 2.clear()：清除字典里的东西，但会保留字典
dic.clear()
print(dic)
# 3.pop() :删除指定键值对,但会返回值
dic['age']=20
print(dic)
print(dic.pop('age'))
print(dic)

#(5) len() 求长度
dic={'name':'李志研','age':20,'height':180}
print(len(dic))
li=[1,2,3,4,5]
print(len(li))
# (6)keys() :返回字典里包含的所有键名
print(dic.keys())
for i in dic.keys():
    print(i,dic[i])
# (7)values() :取出字典里所有的值
print(dic.values())
# (8)items :取出键值对
for i in dic.items():
    print(i,type(i))      #i 是以元组的形式




