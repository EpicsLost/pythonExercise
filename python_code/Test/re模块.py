import re

f = open("account","r")
data = f.read()
print(re.findall("1[0-9]{10}",data))

s = ""