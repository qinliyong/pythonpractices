'''题目描述

Alice 有一个边长为 a 的正方形，Bob 有一个长宽分别为 b,c 的矩形，请你告诉他们俩谁的图形面积更大。
输入格式

仅一行三个正整数 a,b,c
输出格式

输出仅一行一个字符串，若正方形面积大则输出 Alice，否则输出 Bob。
'''

a,b,c = map(int,input().split())
sa = a*a
sb = b*c
if sa > sb:
    print("Alice")
else:
    print("Bob")