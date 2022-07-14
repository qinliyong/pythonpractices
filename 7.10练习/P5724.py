'''题目描述
给出 n 和 n 个整数 ai​，求这 n 个整数中的极差是什么。极差的意思是一组数中的最大值减去最小值的差。
输入格式

第一行输入一个正整数 n，表示整数个数。

第二行输入 n 个整数 a1,a2…an​，以空格隔开。
输出格式

输出一个整数，表示这 n个整数的极差。
'''
n = int(input())

nums = input().split()

for i in range(n):
    nums[i] = int(nums[i])

print(max(nums)-min(nums))