'''题目描述

炎热的夏日，KC 非常的不爽。他宁可忍受北极的寒冷，也不愿忍受厦门的夏天。最近，他开始研究天气的变化。他希望用研究的结果预测未来的天气。

经历千辛万苦，他收集了连续 N(1≤N≤10^6) 的最高气温数据。

现在，他想知道最高气温一直上升的最长连续天数。
输入格式

第 1 行：一个整数 N 。1≤N≤ 10^6

第 2 行：N个空格隔开的整数，表示连续 N 天的最高气温。0≤ 最高气温 ≤10^9 。
输出格式

1 行：一个整数，表示最高气温一直上升的最长连续天数。
'''

n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

lxss = 0
ans = 1
b = []
for i in range(1,n):
    b.append(a[i]-a[i-1])
#print(b)

for i in range(len(b)):
    if b[i] > 0:
        lxss += 1
        if lxss > ans:
            ans = lxss
    else:
        lxss = 0
if ans >1:
    print(ans+1)
else:
    print(1)