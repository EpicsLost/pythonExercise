import re

line = 'S -> aA | bB | dC'
l = re.split("( |->|\n|\||)*", line)
for i in l:
    l.remove('')
print(l)