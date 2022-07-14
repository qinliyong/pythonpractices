'''
用高精度计算出 S=1!+2!+3!+⋯+n!（n≤50）。
输入格式
一个正整数 n。
输出格式
一个正整数 S，表示计算结果。
'''
a = int(input())

jx = 1
sum = 0
for s in range(a+1):
    for i in range(1,s+1):
        jx = jx*i
    #print(jx)
    sum = sum+jx
    jx=1

print(sum-1)
