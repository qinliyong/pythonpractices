'''题目描述

给出三个整数 a,b,c(0≤a,b,c≤100)，要求把这三位整数从小到大排序。
输入格式

输入三个整数 a,b,c，以空格隔开。
输出格式

输出一行，三个整数，表示从小到大排序后的结果。
'''
abc = input().split()
for i in range(len(abc)):
    abc[i] = int(abc[i])
abc.sort()
for i in range(len(abc)):
    print(abc[i],end=" ")