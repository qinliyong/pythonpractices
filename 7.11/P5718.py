'''题目描述

给出 n 和 n 个整数 ai，求这 n 个整数中最小值是什么。
输入格式

第一行输入一个正整数 n，表示数字个数。

第二行输入 n 个非负整数，表示 a1,a2…an，以空格隔开。
输出格式

输出一个非负整数，表示这 n 个非负整数中的最小值。
'''
n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
print(a[0])