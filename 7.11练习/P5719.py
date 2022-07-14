'''题目描述
给定 n 和 k，将从 1 到 n 之间的所有正整数可以分为两类：
A 类数可以被 k 整除（也就是说是 k 的倍数），
而 B 类数不能
请输出这两类数的平均数，精确到小数点后 1 位，用空格隔开。
数据保证两类数的个数都不会是 0。
输入格式
输入两个正整数 n 与 k。
输出格式
输出一行，两个实数，分别表示 A 类数与 B 类数的平均数。精确到小数点后一位。
'''
n,k = map(int,input().split())
a = []
b = []
for i in range(1,n+1):
    if i%k == 0:
        a.append(i)
    else:
        b.append(i)
suma = 0
sumb = 0
for j in range(len(a)):
    suma += a[j]
for j  in range(len(b)):
    sumb += b[j]
avra = suma/len(a)
avrb = sumb/len(b)
print("%.1f"%avra,end=" ")
print("%.1f"%avrb)