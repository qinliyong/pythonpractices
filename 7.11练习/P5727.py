'''题目描述
给出一个正整数 n，然后对这个数字一直进行下面的操作：
如果这个数字是奇数，那么将其乘 3 再加 1，
否则除以 2。
经过若干次循环后，最终都会回到 1。经过验证很大的数字都可以按照这样的方式比变成 1，所以被称为“冰雹猜想”。
例如当 n 是 20，变化的过程是 20→10→5→16→8→4→2→1
根据给定的数字，验证这个猜想，并从最后的 1 开始，倒序输出整个变化序列。
输入格式
输入一个正整数 n。
输出格式
输出若干个由空格隔开的正整数，表示从最后的 1 开始倒序的变化数列。
'''
def caozuo(n):
    a = []
    a.append(n)
    #print(a)
    while(n!=1):
        if n%2 != 0:
            n =(3*n)+1
            a.append(n)
        else:
            n = n//2
            a.append(n)
    #print(a)
    for i in range(len(a)-1,-1,-1):
        print(a[i],end=" ")

n = int(input())
caozuo(n)