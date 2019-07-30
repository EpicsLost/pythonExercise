def put_in():  # 输入文法五元组
    global a, vn, vt, start
    # a=[list('S->AB'),list('S->bC'),list('A->*'),list('A->b'),list('B->*'),list('B->aD'),list('C->AD'),list('C->b'),list('D->aS'),list('D->c')]
    # vn=['S','A','B','C','D']
    # vt=['a','b','c']
    a = [list('E->TA'), list('A->+TA'), list('T->FB'), list('A->*'), list('B->-FB'), list('B->*'), list('F->i'),
         list('F->(E)')]
    vn = ['E', 'A', 'B', 'F', 'T']
    vt = ['+', '-', '(', ')', 'i']
    start = 'E'
    print('文法产生式为：')
    for i in a:
        print(i)


def judge_null():  # 求能推出空串的非终结符
    null = ['*']
    values = [1] * len(vn + vt + null)
    dic = dict(zip(vn + vt + null, values))
    dic['*'] = 0
    for un_relation in range(5):
        for i in a:
            sum = 0
            for j in range(3, len(i)):
                sum = sum + dic[i[j]]
            if sum == 0:
                dic[i[0]] = 0
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
                    if oo == len(j) - 3 and j[3] != '*':  # 若右部全部是能推出空符的非终结符
                        for i1 in range(3, len(j)):
                            f[i] = f[i] | f[vn.index(j[i1])]

                        f[i] = f[i] | {'*'}
                    else:
                        if j[3] in vt:
                            f[i].add(j[3])
                        elif j[3] == '*':
                            f[i].add('*')
                        else:
                            for i1 in range(3, len(j)):
                                if dic[j[i1]] == 0:
                                    if '*' in f[vn.index(j[i1])]:
                                        f[i] = (f[vn.index(j[i1])] | f[i]) - {'*'}
                                    else:
                                        f[i] = (f[vn.index(j[i1])] | f[i])
                                else:
                                    f[i] = (f[vn.index(j[i1])] | f[i])
                                    break

    print('非终结符的FIRST集(E,A,B,F,T)依次为：')
    print(f)


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
        if oo == len(i) - 3 and i[3] != '*':  # 若全部是能推出空符的非终结符
            for j in range(3, len(i)):
                f1[k] = f1[k] | f[vn.index(i[j])]
            f1[k] = f1[k] | {'*'}
        else:
            if i[3] in vt:  # 若是以终结符开头
                f1[k].add(i[3])
            elif i[3] == '*':  # 若是空符
                f1[k].add('*')
            else:
                for j in range(3, len(i)):
                    if dic[i[j]] == 0:
                        f1[k] = (f[vn.index(i[j])] | f1[k]) - {'*'}
                    else:
                        f1[k] = (f[vn.index(i[j])] | f1[k])
                        break
    print('符号串的FIRST集依次为：')
    print(f1)


def index1(li, k):  # 神奇勿动，求在产生式右部某元素在列表第一次出现的位置
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
                                    follow[i] = (follow[i] | f[vn.index(j[index1(j, k) + 1])]) - {'*'}
                                else:
                                    follow[i] = (follow[i] | f[vn.index(j[index1(j, k) + 1])]) - {'*'}
                                    follow[i] = follow[i] | follow[vn.index(j[0])]
    print('follow集依次为：')
    print(follow)


def select():
    dic = judge_null()
    global s
    s = []
    for i in range(len(a)):
        s = s + [set()]
    for i in a:
        k = a.index(i)
        oo = 0
        for j in range(3, len(i)):
            if dic[i[j]] == 0:
                oo = oo + 1
        if oo == len(i) - 3:  # 若全部是能推出空符
            s[k] = (f1[k] - {'*'}) | follow[vn.index(i[0])]
        else:
            s[k] = f1[k]
    print('select集依次为：')
    print(s)


def judge():  # 判断文法是不是LL1文法
    b = set()
    zz = 0
    for i in range(len(a)):
        for k in range(len(a)):
            if a[i][0] == a[k][0] and i != k:
                b = s[i] & s[k]
                if len(b) != 0:
                    print('不是LL（1）文法,因为：')
                    print(a[i], '和', a[k], '的select集的交集不为空')
                    zz = 1
    if zz == 1:
        return 1
    else:
        return 0


def pipei():  # 匹配字符串
    if judge() == 1:
        return 0
    c = list(input('请输入待匹配子串'))
    st = ['#', start]
    while True:
        i = 0
        for k in range(len(s)):
            if st[len(st) - 1] == a[k][0] and c[0] in s[k]:
                i = 1
                st.pop()
                for j in range(3, len(a[k])):
                    st = st + [a[k][len(a[k]) - j + 2]]
                if st[len(st) - 1] == '*':
                    st.pop()
                if st[len(st) - 1] == c[0]:
                    if c == ['#'] and st == ['#']:
                        print('Accept')
                        return 0
                    c.remove(c[0])
                    st.pop()
                if c == ['#'] and st == ['#']:
                    print('Accept')
                    return 0
        if i == 0:
            print('error')
            return 0


def run():
    put_in()
    first()
    first_chuan()
    follow_()
    select()
    judge()
    pipei()


run()