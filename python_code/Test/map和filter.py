a = [1,2,3,4,5,6,7]
b = map(lambda x:x+2,a)
print(list(b))

a = [1,2,3,4,5,6,7]
b = filter(lambda x:x+2,a)
print(list(b))

a = [1,2,3,4,5,6,7]
b = map(lambda x:x>2,a)
print(list(b))

a = [1,2,3,4,5,6,7]
b = filter(lambda x:x>2,a)
print(list(b))

#filter是通过生True和False组成的迭代器将可迭代对象中不符合条件的元素过滤掉，
#map返回的是True和False组成的迭代器