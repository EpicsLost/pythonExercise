import itchat

itchat.auto_login(hotReload=True) #自动登录
wxFriends = itchat.get_friends(update=True)#获取所有好友信息
sex = []
man = woman = sum = 0

for friend in wxFriends[0:]:
    sex = friend["Sex"]
    if sex == 1:
        man += 1
    elif sex == 0:
        woman += 1
sum = man + woman
print("微信中男性人数为：",man)
print("微信中女性人数为：",woman)
print("微信中的总人数为：",sum)