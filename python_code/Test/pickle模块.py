import pickle

"""
    支持python中的所有类型
    但是只能在python中使用
"""
# d = {"name":"alex","age":"22"}
# l = [1,2,3,4,"rain"]
#
# pk = open("data.pkl","wb")
# pickle.dump(d,pk)
# print(pickle.dumps(d))

# f = open("data.pkl","rb")
# d = pickle.load(f)
# print(d)

def sayhi():
    print("Hello")

pickle.dumps(sayhi)