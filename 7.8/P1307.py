'''
题目描述
给定一个整数，请将该数各个位上数字反转得到一个新数。
新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零（参见样例2）。
输入格式
一个整数 N
输出格式
一个整数，表示反转后的新数。
'''
n = int(input())
if n >=0:
    x=0
    while(n):
        x=x*10
        x=x+n%10
        n=n//10
    print(x)
elif n < 0:
    m = -n
    y=0
    while(m):
        y=y*10
        y=y+m%10
        m=m//10
    print(-y)