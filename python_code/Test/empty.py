
s = "aaacccdddd"
dict = {}
dict = set([(i,s.count(i)) for i in s])
a = sorted(dict,key = lambda x:x[1])
print(dict)

