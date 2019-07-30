#1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，
# 如果该函数没有描述文档，则返回"not found"
def get_fundoc(func):
    #使用callable判断是否能被调用
    # if not callable(func):
    #     return 'the func not function'
    # elif str(type(func)) == "<type 'classobj'>" or str(type(func)) == "<type 'module'>":
    #     return 'this not a function'
    # else:
        if func.__doc__ == None:
            print('not doc')
        else:
            print( func.__doc__)

get_fundoc(print)

#2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
def get_cjsum():
    sum = 0
    for i in range(1,101):
        sum += i*i
    return sum

print(get_cjsum())

#3 定义一个方法list_info(list), 参数list为列表对象，
# 怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值
a = [1,2,3]
def list_info(list):
    a = list[:]
    list[0]="test123"
    print(a)
list_info(a)

#4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，
# 如果可以调用则返回该函数名(类型为str)，否则返回 “fun is not function"。
def get_funcname(func):
    if not callable(func):
        return "func is not function"
    else:
        return func.__name__

print(get_funcname(list_info(a)))