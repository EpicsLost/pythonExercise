def put_in():  # 输入文法五元组
    global a, vn, vt, start
    # a=[list('S->AB'),list('S->bC'),list('A->*'),list('A->b'),list('B->*'),list('B->aD'),list('C->AD'),list('C->b'),list('D->aS'),list('D->c')]
    # vn=['S','A','B','C','D']
    # vt=['a','b','c']
    a = [list('E->TA'), list('A->+TA'), list('T->FB'), list('A->&'), list('B->*FB'), list('B->&'), list('F->i'),
         list('F->(E)')]
    vn = ['E', 'A', 'B', 'F', 'T']
    vt = ['+', '*', '(', ')', 'i']
    start = 'E'
    print('文法产生式为：')
    for i in a:
        print(i)


def judge_null():  # 求能推出空串的非终结符
    null = ['&']
    values = [1] * len(vn + vt + null)
    dic = dict(zip(vn + vt + null, values))
    dic['&'] = 0
    for un_relation in range(5):
        for i in a:
            sum = 0
            for j in range(3, len(i)):
                sum = sum + dic[i[j]]
            if sum == 0:
                dic[i[0]] = 0
    #print(dic)
    return dic


def first():  # 求每一个非终结符的FIRST集
    dic = judge_null()
    global f
    f = []
    for i in range(len(vn)):
        f = f + [set()]
    for ji in range(5):
        for i in range(len(vn)):
            for j in a:
                if vn[i] == j[0]:
                    oo = 0
                    for i1 in range(3, len(j)):
                        if dic[j[i1]] == 0:
                            oo = oo + 1
                    if oo == len(j) - 3 and j[3] != '&':  # 若右部全部是能推出空符的非终结符
                        for i1 in range(3, len(j)):
                            f[i] = f[i] | f[vn.index(j[i1])]

                        f[i] = f[i] | {'&'}
                    else:
                        if j[3] in vt:
                            f[i].add(j[3])
                        elif j[3] == '&':
                            f[i].add('&')
                        else:
                            for i1 in range(3, len(j)):
                                if dic[j[i1]] == 0:
                                    if '&' in f[vn.index(j[i1])]:
                                        f[i] = (f[vn.index(j[i1])] | f[i]) - {'&'}
                                    else:
                                        f[i] = (f[vn.index(j[i1])] | f[i])
                                else:
                                    f[i] = (f[vn.index(j[i1])] | f[i])
                                    break

    print('非终结符的FIRST集(E,A,B,F,T)依次为：')

    return f


def first_chuan():  # 求每一个产生式右部符号串的FIRST集
    global f1
    dic = judge_null()
    f1 = []
    for i in range(len(a)):
        f1 = f1 + [set()]
    for i in a:
        k = a.index(i)
        oo = 0
        for j in range(3, len(i)):
            if dic[i[j]] == 0:
                oo = oo + 1
        if oo == len(i) - 3 and i[3] != '&':  # 若全部是能推出空符的非终结符
            for j in range(3, len(i)):
                f1[k] = f1[k] | f[vn.index(i[j])]
            f1[k] = f1[k] | {'&'}
        else:
            if i[3] in vt:  # 若是以终结符开头
                f1[k].add(i[3])
            elif i[3] == '&':  # 若是空符
                f1[k].add('&')
            else:
                for j in range(3, len(i)):
                    if dic[i[j]] == 0:
                        f1[k] = (f[vn.index(i[j])] | f1[k]) - {'&'}
                    else:
                        f1[k] = (f[vn.index(i[j])] | f1[k])
                        break
    print('符号串的FIRST集依次为：')
    #print(f1)
    return f1


def index1(li, k):  # 求在产生式右部某元素在列表第一次出现的位置
    for i in range(3, len(li)):
        if li[i] == k:
            return i


def follow_():  # 计算非终结符的FOLLOW集
    dic = judge_null()
    global follow
    follow = []
    for i in range(len(vn)):
        follow = follow + [set()]
    follow[vn.index(start)] = follow[vn.index(start)] | {'#'}
    for iii in range(5):
        for i in range(len(vn)):
            for j in a:
                for k in j[3:]:
                    if k == vn[i]:
                        if index1(j, k) == len(j) - 1:
                            follow[i] = follow[i] | follow[vn.index(j[0])]
                        else:
                            if j[index1(j, k) + 1] in vt:
                                follow[i] = follow[i] | {j[index1(j, k) + 1]}
                            else:
                                if dic[j[index1(j, k) + 1]] == 1:
                                    follow[i] = (follow[i] | f[vn.index(j[index1(j, k) + 1])]) - {'&'}
                                else:
                                    follow[i] = (follow[i] | f[vn.index(j[index1(j, k) + 1])]) - {'&'}
                                    follow[i] = follow[i] | follow[vn.index(j[0])]
    print('follow集(E,A,B,F,T)依次为：')
    #print(follow)
    return follow

Table = dict()

def getTable():
    # vn = ['E', 'A', 'B', 'F', 'T']
    # vt = ['+', '*', '(', ')', 'i']
    vt.extend("#")
    for i in a:
        Table[i[0]] = dict()
        for e in vt:
            Table[i[0]][e] = None

    aa = {}
    for i in a:
        # print(i[:1])
        # print("".join(i[3:]))
        if "".join(i[:1]) not in aa:
            aa["".join(i[:1])] = list("".join(i[3:]))

    list1 = []
    for i in a:
        list1.append("".join(i))

    copy_list = list1
    for j in list1:
        if j[3] == "&":
            copy_list.remove(j)

    copy_a = a
    for j in a:
        if j[3] == "&":
            copy_a.remove(j)

    for k in aa:
        #chuan是产生式右边
        chuan = "".join(aa.get(k))
        for i in list(fuhaochuanDic[chuan]):
            for e in vt:
                if i == e:
                    for j in range(0, len(copy_list)):
                        if copy_a[j][0] == k:
                            Table[k][e] = copy_list[j]



    print("预测分析表：\n",Table)



if __name__ == "__main__":
    put_in()

    f = first()
    f_list = []
    for i in range(0,len(f)):
        f_list.append(list(f[i]))
    print("F_FIRST:",f_list)
    first = dict(zip(vn, f_list))
    print("first:",first)

    aa = {}
    for i in a:
        if "".join(i[:1]) not in aa:
            aa["".join(i[:1])] = list("".join(i[3:]))
    print("aa:",aa)
    for k in aa:
        pro = aa[k]
        print(first[k])

    f1 = first_chuan()
    print(f1)
    fuhaochuan = []
    for i in a:
        fuhaochuan.append("".join(i[3:]))

    fuhaochuanDic = dict(zip(fuhaochuan,f1))


    f2 = follow_()
    follow = dict(zip(vn,f2))
    print(follow)
    print(a)

    list1 = []
    for i in a:
        list1.append("".join(i))

    print("list1:",list1)
    print("...",list(fuhaochuanDic["TA"]))
    print("符号串：",fuhaochuan)
    print("符号串dic", fuhaochuanDic)

    for i in range(0, len(list1)):
        print(a[i][0],end=" ")
    print("\n")

    print("aa:",aa)
    for k in aa:
        print("".join(aa.get(k)),end=" ")
        print(fuhaochuanDic["".join(aa.get(k))],end=" ")

    getTable()



