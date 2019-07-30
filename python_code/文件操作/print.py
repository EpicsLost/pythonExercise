# msg = "又回到最初的起点，记忆中你青涩的脸"
# f = open("print_tofile.txt","w")
# print(msg,file = f)

dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4, 'IX':9, 'XL':40, 'XC':90,'CD':400, 'CM':900}
s = input()
num = 0
ispass = False
length = len(s)

for i in range(length):
    if ispass:
        ispass = False
        continue
    if s[i] in dic and s[i:i+2] not in dic:
        num = num + dic[s[i]]
        ispass=False
        continue
    if s[i:i+2] in dic:
        num = num + dic[s[i:i+2]]
        ispass = True

print(num)