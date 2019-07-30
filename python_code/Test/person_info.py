name = input("请输入用户名：")
password = input("请输入密码：")

def search(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if name in list[i][0] and password in list[i][1]:
                print("---个人信息如下---")
                print("name:",list[i][0])
                print("age :",list[i][2])
                print("pro :",list[i][3])
                print("occ :",list[i][4])
                break


f = open("account","r+")
data = f.readlines()
list = []
for i in data:
    data = i.strip("\n")
    temp = data.split(",")
    list.append(temp)

print("1.修改个人信息")
print("2.查看个人信息")
print("3.修改密码")

dic = {"1":"1",
       "2":"2",
       "3":"2"}
num = input("请输入你想要操作的步骤：")
if num == dic["2"]:
    search(list)
