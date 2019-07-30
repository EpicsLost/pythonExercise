import json

data = {
    "roles":[
        {"role":"monster","type":"pig"},
        {"role":"hero","type":"spiderman"}
    ]
}
"""
    支持str,int,tuple,list,dict
"""

#dumps：接收的第一个参数是对象字典
#dump ：接收的第一个参数是对象字典，第二个参数是文件对象
# d = json.dumps(data)#仅转化成字符串存到内存中
# print(d)

# f = open("test.json","w")#转化成字符串并写入文件中
# json.dump(data,f)

# d = json.dumps(data)
# d1 = json.loads(d)
# print(d1["roles"])

#load:读取的是含有json的文件数据
#loads:读取的事json字符串
f = open("test.json","r")
data = json.loads(f.read())#data = json.load(f)
print(type(data))
