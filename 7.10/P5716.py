'''
题目描述

输入年份和月份，输出这一年的这一月有多少天。需要考虑闰年。
输入格式

输入两个正整数，分别表示年份 y 和月数 m，以空格隔开。
输出格式

输出一行一个正整数，表示这个月有多少天。
'''
def runnian(y):
    if y%100 != 0:
        if y%4 == 0:
            return True
        else:
            return False
    else:
        if y%400 == 0:
            return True
        else:
            return False
def manyday(y,m):
    if m == 1 or m == 3 or m == 5 or m ==7 or m == 8 or m == 10 or m ==12:
        print("31")
    elif m == 4 or m == 6 or m == 9 or m ==11:
        print("30")
    elif m ==2:
        if runnian(y):
            print("29")
        else:
            print("28")
y,m = map(int,input().split())
manyday(y,m)
