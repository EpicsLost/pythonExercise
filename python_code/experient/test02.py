from scipy.special import comb, perm
# def b(i):
#     if i == 1:
#         return i
#     else:
#         return i*b(i-1)
# def c(n,i):
#     first = b(n)
#     second = b(i)
#     third = b(n-i)
#     return first/(second*third)
#
# print(c(5,3))
def bagging(n,p):
    s = 0
    for i in range(n // 2 + 1, n + 1):
        s+=comb(n,i) * p ** i * (1-p) ** (n-i)
    return s

if __name__ == '__main__':
    for t in range(10,101,10):
        print(t,"次采样正确率:",bagging(t,0.6))
