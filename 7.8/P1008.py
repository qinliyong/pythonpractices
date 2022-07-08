'''
题目描述
将 1,2,…,9 共 9个数分成 3组，分别组成 3个三位数，且使这 3 个三位数构成 1:2:3的比例，试求出所有满足条件的 3 个三位数。
输入格式
无
输出格式
若干行，每行 3 个数字。按照每行第 1 个数字升序排列。
'''
s = [1,2,3,4,5,6,7,8,9]
for a in range(100,333):
    b = 2*a
    c = 3*a
    s[0]=a//100
    s[1]=a%100//10
    s[2]=a%10
    s[3]=b//100
    s[4]=b%100//10
    s[5]=b%10
    s[6]=c//100
    s[7]=c%100//10
    s[8]=c%10
    s2=list(dict.fromkeys(s))
    if len(s2) == len(s):
        #print(s)
        for i in range(3):
            print(s[i],end="")
        print(" ",end="")
        for i in range(3,6):
            print(s[i],end="")
        print(" ",end="")
        for i in range(6,9):
            print(s[i],end="")
        print("")
