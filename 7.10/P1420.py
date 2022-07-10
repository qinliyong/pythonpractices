'''题目描述

输入长度为 n 的一个正整数序列，要求输出序列中最长连号的长度。

连号指在序列中，从小到大的连续自然数。
输入格式

第一行，一个整数 n。

第二行，n 个整数 ai​，之间用空格隔开。
输出格式

一个数，最长连号的个数。
'''

n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
#print(a[2]-a[1])
maxlian = 0
ans = 1
b = []
for i in range(1,n):
    b.append(a[i]-a[i-1])
#print(b)

for i in range(len(b)):
    if b[i] == 1:
        maxlian += 1
        if maxlian > ans:
            ans = maxlian
    else:
        maxlian = 0
if ans >1:
    print(ans+1)
else:
    print("1")