'''题目描述
模仿例题，打印出不同方向的正方形，然后打印三角形矩阵。中间有个空行。
输入格式
输入矩阵的规模，不超过 9。
输出格式
输出矩形和正方形
输入输出样例
输入 
4
输出 
01020304
05060708
09101112
13141516

      01
    0203
  040506
07080910
'''
n=int(input())
num=1
m=n
for m in range(m+1,1,-1):
    for j in range(1,n+1):
        print("%02d"%num,end="")
        num += 1 
    print("")    
print("")

num=1
m=n
for i in range(1,m+1):
    for k in range(1,n):
        print("  ",end="")
    for j in range(n,m+1):
        print("%02d"%num,end="")  
        num += 1 
    n=n-1
    print("")   