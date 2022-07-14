'''题目描述

因为 151 既是一个质数又是一个回文数（从左到右和从右到左是看一样的），所以 151是回文质数。

写一个程序来找出范围 [a,b](5≤a<b≤100000000)（一亿）间的所有回文质数。
输入格式

第一行输入两个正整数 a 和 b。
输出格式

输出一个回文质数的列表，一行一个。
'''
'''
hint:
1.偶数位数回文数（除11）必定不是质数（自行百度），所以只要运行到10000000。
2.偶数肯定不是质数。'''

def isZhishu(num):
    for i in range(2,num):
        if (num % i) == 0:
            return 0
    return num
#abcdedcba
#abcddcba
#abcdcba
#abccba
#abcba
#abba
#aba
#aa
#a
hws12 = [3,5,7,11]
hws3 = []
hws5 = []
hws7 = []

def Huiwenshu3():
    for a in range(1,10,2):
        for b in range(10):
            hws3.append(100*a+10*b+a)


def Huiwenshu5():
    for a in range(1,10,2):
        for b in range(10):
            for c in range(10):
                hws5.append(10000*a+1000*b+100*c+10*b+a)

def Huiwenshu7():
    for a in range(1,10,2):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    hws7.append(1000000*a+100000*b+10000*c+1000*d+100*c+10*b+a)
             

Huiwenshu3()
Huiwenshu5()
Huiwenshu7()

hws = hws12+hws3+hws5+hws7
#print(hws)
zhishu = []
for i in range(len(hws)):
    zhishu.append(isZhishu(hws[i]))

huiwenzhishu = []
for i in range(len(zhishu)):
    if zhishu[i] != 0:
        huiwenzhishu.append(zhishu[i])

print(huiwenzhishu)
