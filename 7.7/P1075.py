'''
题目描述
已知正整数n是两个不同的质数的乘积，试求出两者中较大的那个质数。
输入格式
一个正整数n。
输出格式
一个正整数p，即较大的那个质数。
'''
# n = int(input())
# p = []
# for i in range(1,n):
#     if n%i == 0 :
#         p.append(i)
# p.sort(reverse=True)
# print(p)

n = int(input())
for i in range(2,n):
    if n%i == 0 :
        print(int(n/i))
        break