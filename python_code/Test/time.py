import time

a = time.localtime()#返回当前本机时间
print(a)
print(a.tm_year)

print(time.time())#返回时间戳

b = time.strftime("%Y-%m-%d %H-%M-%S")#格式化输出时间
print(b)

d = time.strftime("%Y-%m-%d %H:%M:%S %U")#最后一个返回的事当前周数
print(d)

f = time.strftime("%A")#星期几
print(f)

g = time.strftime("%B")#月份
print(g)

#可用于时间相减
c = time.strptime(b,"%Y-%m-%d %H-%M-%S")#返回时间对象
print(c)
print(time.mktime(c))

#将时间转化为时间戳
t = time.strftime("%Y-%m-%d")
t1 = time.strptime(t,"%Y-%m-%d")
t2 = time.mktime(t1)
print(t2)

#将时间戳转化成时间
t3 = time.time()
t4 = time.localtime(t3)
t5 = time.strftime("%Y-%m-%d",t4)
print(t5)


