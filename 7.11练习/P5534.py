'''题目描述
小 X 给了你一个等差数列的前两项以及项数，请你求出这个等差数列各项之和。

一行 3 个整数 a1,a2,n，表示等差数列的第 1,2 项以及项数。

输出格式
一行一个整数，表示答案。
'''
a1,a2,n = map(int,input().split())
q = a2 - a1
a = []
for i in range(n):
    a.append(a1+q*i)
sum = 0
for i in range(len(a)):
    sum += a[i]
print(sum)


