'''题目描述
求 n!中某个数码出现的次数。
输入格式
第一行为 t(t≤10)，表示数据组数。接下来 t 行，每行一个正整数 n(n≤1000)和数码 a。
输出格式
对于每组数据，输出一个整数，表示 n! 中 a出现的次数。
输入输出样例
输入 
2
5 2
7 0
输出 
1
2
'''
#5! : 120  1个2
#7! : 5040 2个0

def jiecheng(n):
    jc = 1
    for i in range(1,n+1):
        jc *= i
    return(jc)

t = int(input())
n = []
a = []
for i in range(t):
    na = input().split()
    n.append(int(na[0]))
    a.append(na[1])
# print(n)
# print(a)
njc = []
for i in range(len(n)):
    njc.append(str(jiecheng(n[i])))
#print(njc)
c = []

for i in range(len(njc)):
    count = 0
    for j in range(len(njc[i])):
        if a[i] == (njc[i])[j]:
            count += 1
    c.append(count)
for i in range(len(c)):
    print(c[i])
