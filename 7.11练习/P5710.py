'''题目描述
一些整数可能拥有以下的性质：

    性质 1：是偶数；
    性质 2：大于 4 且不大于 12。

小 A 喜欢这两个性质同时成立的整数；
Uim 喜欢这至少符合其中一种性质的整数；
八尾勇喜欢刚好有符合其中一个性质的整数；
正妹喜欢不符合这两个性质的整数。现在给出一个整数 x，请问他们是否喜欢这个整数？
输入格式

输入一个整数 x(0≤x≤1000)
输出格式

输出这 4 个人是否喜欢这个数字，如果喜欢则输出 1，否则输出 0，用空格分隔。输出顺序为：小 A、Uim、八尾勇、正妹。
'''
def isone(n):
    if n%2 == 0:
        return True
    else:
        return False

def istwo(n):
    if 4< n <=12:
        return True
    else:
        return False

n = int(input())
if isone(n) and istwo(n):
    a=1
else:
    a=0

if isone(n) or istwo(n):
    u=1
else:
    u=0

if isone(n) and not istwo(n):
    b=1
elif istwo(n) and not isone(n):
    b=1
else:
    b=0

if isone(n) or istwo(n):
    z=0
else:
    z=1

print(a,u,b,z)