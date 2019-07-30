FIRST = dict()
FOLLOW = dict()
LAN = dict()

def get_lan(file_path):
    fo = open(file_path, "r")  # 读文法文件
    for line in fo.readlines():
        pos1 = line.index("-")
        pos2 = pos1+1
        splitlist = line[pos2:].replace("\n", "").split("|")
        LAN[line[:pos1]] = splitlist

    return LAN

def get_first(LAN):
    for k in LAN:
        l = LAN[k]
        FIRST[k] = list()
        for s in l:
            if not (s[0].isupper()):
                FIRST[k].append(s[0])
                break

    for k in LAN:
        l = LAN[k]
        for s in l:
            if not (s[0].isupper()):

                FIRST[k].extend(s[0])
                FIRST[k] = list(set(FIRST[k]))  # 去重
            else:
                for i in LAN[s[0]]:
                    if not (i[0].isupper()):
                        FIRST[k].extend(i[0])
    print("文法为：%s" % LAN)
    print("FIRST集为：%s" % FIRST)


if(__name__ == '__main__'):
    lan = get_lan("文法.txt")
    get_first(lan)