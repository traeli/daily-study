if __name__ == '__main__':
    print("这是我的第一天学习")

#.1.if
#格式： if 判断条件 :
#          输出语句
score=input("请输入你的成绩：")         #注意：input输入是字符串类型
if score=='100':
    print('very good')
if score=='60':
    print('捞逼')

print('=====================')
#.2.比较运算符
#== ！=
#.3.逻辑运算符
#（1）and:表示和       （2）or：表示或         （3）not：非
print(score>'60')
print(not 3>9)
#.4.三目运算符
# 基本格式：条件为true的结果 if 判断条件 else 条件为假的结果
a=8
b=10
print('a<b') if a<b else print('a>b')
print('=====================')

#.5.while循环
#基本格式：while 判断:
#               循环体
#               条件改变
a=100
while a>90:
    print(a)
    a-=1
# 死循环:只要条件不是0或者false就是死循环
i=1
num=0
while i<=100:
    num+=i
    i+=1
print(num)

print('=====================')
#.6.for 循环
#(1)基本格式： for 临时变量 in 可迭代对象:             注意：字符串是可迭代对象
#              循环体
str="Hello World"
for i in str:
    print(i)
#(2)range()
#1.只写一个数 就是循环的次数 默认从0开始  2.写两个数 从左边开始 右边结束
for i in range(5):
    print(i)
for i in range(1,5):
    print(i)

sum=0
for i in range(101):
    sum+=i
print(sum)
#.6.break和continue关键字（只能在循环中用）
# break:终止循环    continue：跳过当前循环，进行下次循环

#.7.字符串编码 encode:编码  decode:解码
#（1）Unicode:所有字符都是两个字节
#（2）UTF-8
a='Hello'
print(a,type(a))
a1=a.encode()
print(type(a1),a1)
a2=a1.decode()
print(a2,type(a2))



