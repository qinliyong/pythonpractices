'''题目描述
小 A 有一个质数口袋，里面可以装各个质数。他从 2 开始，依次判断各个自然数是不是质数，如果是质数就会把这个数字装入口袋。
口袋的负载量就是口袋里的所有数字之和。但是口袋的承重量有限，不能装得下总和超过 L 的质数。
给出 L，请问口袋里能装下几个质数？将这些质数从小往大输出，然后输出最多能装下的质数个数，所有数字之间有一空行。
输入格式
一行一个正整数 L。
输出格式
将这些质数从小往大输出，然后输出最多能装下的质数个数，所有数字之间有一空行。
'''
def isZhishu(num):
    for i in range(2,num):
        if (num % i) == 0:
            return 0
    return num

l = int(input())
pocket = []
for i in range(2,l+1):
    pocket.append(isZhishu(i))
# print(pocket)
# 13
# [2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13]
sum = 0
real_pocket = []
for i in range(len(pocket)):
    sum += pocket[i]
    if sum > l:
        break
    elif pocket[i] != 0:
        real_pocket.append(pocket[i])
#print(real_pocket)
for i in range(len(real_pocket)):
    print(real_pocket[i])
print(len(real_pocket))
