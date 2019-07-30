#1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。
# 其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。

def get_num(num):
    if type(num) !=list:
        return "您传入的不是列表！"
    else:
        for i in num:
            if not isinstance(i,int):
                return"您传入的不是整数!"
        return list(filter(lambda x:x%2==0,num))
print(get_num([22,41,32,45,113]))
print(get_num((12,342,534,56,67,7)))
print(get_num(['2','dsa',345,2,4,6,9]))

#2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。
# 提示（可以了解python的urllib模块）。
import urllib.request

def get_page(url):
    res = urllib.request.Request(url)
    f = urllib.request.urlopen(res)
    data = f.read()
    file = open("./1.html","wb")
    file.write(data)
    file.close()
    print(f.status)

get_page("http://www.baidu.com")


#3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def func(*num):
    max_value = []
    for i in num:
        if not isinstance(i,list):
            return "您传入的不是列表参数！"
        else:
            for j in i:
                max_value.append(j)
    a = max(max_value)
    return a
print(func([1,2,3,4,5],(5,2,7,9,1)))
print(func([1,2,3,4,5],[5,2,7,9,1]))

#4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，
# 如果没有文件夹则返回"Not dir"。
import os

def get_dir(f):
    dir_list = os.listdir(f)
    for i in dir_list:
        print(i)

get_dir("f:")