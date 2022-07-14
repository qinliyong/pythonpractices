'''题目描述

学校正在选举学生会成员，有 n(n≤999) 名候选人，每名候选人编号分别从 1 到 n，现在收集到了 m(m<=2000000) 张选票，每张选票都写了一个候选人编号。
现在想把这些堆积如山的选票按照投票数字从小到大排序。
输入格式
输入 n 和 m 以及 m 个选票上的数字。
输出格式
求出排序后的选票编号。
'''

n,m = map(int,input().split())
t = input().split()
for i in range(m):
    t[i] = int(t[i])
t.sort()
for i in range(m):
    print(t[i],end=" ")