'''
题目描述
小玉开心的在游泳，可是她很快难过的发现，自己的力气不够，游泳好累哦。
已知小玉第一步能游2米，可是随着越来越累，力气越来越小，她接下来的每一步都只能游出上一步距离的98%。
现在小玉想知道，如果要游到距离x米的地方，她需要游多少步呢。请你编程解决这个问题。
输入格式
输入一个数字（不一定是整数，小于100m），表示要游的目标距离。
输出格式
输出一个整数，表示小玉一共需要游多少步。
'''
#等比数列 2 ， 2*0.98 ， 2*0.98*0.98 ...
# 2*(1-0.98**n)/(1-0.98)
a = float(input())
for i in range(1,1000):
    l = 2*(1-0.98**i)/(1-0.98)
    if l > a:
        print(i)
        exit()

