'''题目描述

输入一组勾股数 a,b,c（a≠b≠c），用分数格式输出其较小锐角的正弦值。（要求约分。）
输入格式

一行，包含三个正整数，即勾股数 a,b,c（无大小顺序）。
输出格式

一行，包含一个分数，即较小锐角的正弦值

'''

abc = input().split()
for i in range(3):
    abc[i] = int(abc[i])
abc.sort()
#print(abc)
a = abc[0] #较短直角边
b = abc[1]
c = abc[2] #斜边
#sinA = a/c
#求公约数
m = max(a, c)
n = min(a, c)
r = m % n
while r != 0:
    m = n
    n = r
    r = m % n
#最大公约数n
a1 = a//n
c1 = c//n
print(str(a1)+"/"+str(c1))