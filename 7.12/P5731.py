'''题目描述
给出 n，请输出一个直角边长度是 n 的数字直角三角形。所有数字都是 2 位组成的，如果没有 2 位则加上前导 0。
输入格式
输入一个正整数 n。
输出格式
输出如题目要求的数字直角三角形。
输入输出样例
输入 5
输出
0102030405
06070809
101112
1314
15
说明/提示
数据保证，1≤n≤13
'''
# n=int(input())
# m=n
# #m行n列
# num=1
# for i in range(1,m+1):#1-m行
#     for j in range(1,n+1):#1-n列
#         print("%02d"%num,end="")#格式化输出num
#         num += 1   #num自增1
#     n=n-1
#     print("")    #行打印完毕，换行，下一行n-1

n=int(input())
num=1
for n in range(n+1,1,-1):
    for j in range(1,n):
        print("%02d"%num,end="")
        num += 1 
    print("")    