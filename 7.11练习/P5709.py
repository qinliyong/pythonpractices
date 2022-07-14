'''题目描述

八尾勇喜欢吃苹果。她现在有 m（1≤m≤100）个苹果，吃完一个苹果需要花费 t（0≤t≤100）分钟，吃完一个后立刻开始吃下一个。
现在时间过去了 s（1≤s≤100）分钟，请问她还有几个完整的苹果？
输入格式

输入三个非负整数表示 m,t,s
输出格式

输出一个整数表示答案。
'''
m,t,s = map(int,input().split())
if t == 0 :
    print(0)
    exit()
if s%t == 0:
    eat = s//t
else:
    eat =(s//t)+1
apple = m - eat
if apple <= 0:
    print(0)
    exit()
else:
    print(apple)