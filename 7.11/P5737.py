'''题目描述
输入 x,y，输出 [x,y]区间中闰年个数，并在下一行输出所有闰年年份数字，使用空格隔开。
输入格式
输入两个正整数 x,y，以空格隔开。
输出格式
第一行输出一个正整数，表示 [x,y] 区间中闰年个数。
第二行输出若干个正整数，按照年份单调递增的顺序输出所有闰年年份数字。
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

x,y = map(int,input().split())
count = 0
for i in range(x,y+1):
    if runnian(i) == True:
        count += 1
print(count)
for i in range(x,y+1):
    if runnian(i) == True:
        print(i,end=" ")
