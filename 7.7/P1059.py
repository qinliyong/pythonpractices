'''
题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，
他先用计算机生成了N个1到1000之间的随机整数(N≤100)，对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。
然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。
输入格式
输入有两行，第1行为1个正整数，表示所生成的随机数的个数N
第2行有N个用空格隔开的正整数，为所产生的随机数。
输出格式
输出也是两行，第1行为1个正整数M，表示不相同的随机数的个数。
第2行为M个用空格隔开的正整数，为从小到大排好序的不相同的随机数
'''
n = int(input())
n_list = input().split()
for i in range(n):
    n_list[i]=int(n_list[i])
#print(n_list)
new_list = list(dict.fromkeys(n_list))
#print(new_list)
m = len(new_list)
print(m)
new_list.sort()
for i in range(len(new_list)):
    print(new_list[i],end=" ")
