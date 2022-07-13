'''题目描述

现在有 n(n≤1000)位评委给选手打分，分值从 0 到 10。需要去掉一个最高分，去掉一个最低分（如果有多个最高或者最低分，也只需要去掉一个），
剩下的评分的平均数就是这位选手的得分。现在输入评委人数和他们的打分，请输出选手的最后得分，精确到 2 位小数。
输入格式

第一行输入一个正整数 n，表示有 n 个评委。

第二行输入 n 个正整数，第 i 个正整数表示第 i个评委打出的分值。
输出格式

输出一行一个两位小数，表示选手的最后得分。
'''
n = int(input())
score = input().split()
for i in range(n):
    score[i] = int(score[i])

total_score = 0
for i in range(n):
    total_score += score[i]

total_score = total_score - max(score) - min(score)
final = total_score/(n-2)
print('%.2f'%final)