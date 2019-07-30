# L = ['Admin','anny','LUCY','sanDY']
# def change(name):
#     return name.capitalize()
# print(list(map(change,L)))


# def fib(x):
#     if x == 1 or x == 2:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
#
# print(fib(24))

# def hanoi(n,x,y,z):
#     if n == 1:
#         print(x,"--->",z)
#     else:
#         hanoi(n-1,x,z,y)
#         print(x,"--->",z)
#         hanoi(n-1,y,x,z)
# hanoi(5,'x','y','z')

dic = {}
dic1 = dic.fromkeys([1,2,3],"赞")

for i in dic1.keys():
    print(i)
for i in dic1.items():
    print(i)
print(dic.get(23))
dic = dic.get(23,'好')
print(dic)
