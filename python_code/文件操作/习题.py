a = "aAsmr3idd4bgs7Dlsf9eAF"
#1.1 请将a字符串的大写改为小写，小写改为大写。
print(a.swapcase())
#1.2 请将a字符串的数字取出，并输出成一个新的字符串。
str1 = [x for x in a if x.isdigit()]
print("".join(str1))
#1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
A_low = a.lower()
str2 = [(x,A_low.count(x)) for x in set(A_low)]
print(dict(str2))
#1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
str3 = list(set(a))
str3.sort(key = a.index)
print("".join(str3))
#1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
print(a[::-1])
#1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。
#   （保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
str4 = [x for x in a if x.isalpha()]
up = []
low = []
for i in str4:
    if i.islower():
        low.append(i)
    elif i.isupper():
        up.append(i)
    else:
        pass
for j in up:
    j_low = j.lower()
    if j_low in low:
        low.insert(low.index(j_low),j)
print(low)
#1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
print(set("boy").issubset(a))
#1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，
#    请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
print(set(['boy','girl','bird','dirty']).issubset(a))
#1.9 输出a字符串出现频率最高的字母
str5 = [(x,a.count(x)) for x in a]
str6 = str5.sort(key=lambda k:k[1],reverse=True)
print(str5[0][0])


#.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.
a = [1,2,3,6,8,9,10,14,17]
a = [str(i) for i in a]
b = "".join(a)
print(b)
