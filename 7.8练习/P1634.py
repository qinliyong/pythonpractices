'''
题目描述
禽兽患传染病了。一个禽兽会每轮传染 x 个禽兽。试问n 轮传染后有多少禽兽被传染？
输入格式
两个非负整数 x 和 n。
输出格式
一个整数，即被传染的禽兽数。
'''
#x=10 , n=2
#1  1+1*10=11   11+11*10=121    
x,n = map(int,input().split())
sum = 1
for i in range(1,n+1):
    sum = sum+x*sum
print(sum)
