'''
手机键盘要按出英文字母就必须要按数字键多下。例如要按出 x 就得按 9 两下，第一下会出 w，而第二下会把 w 变成 x。0 键按一下会出一个空格。

你的任务是读取若干句只包含英文小写字母和空格的句子，求出要在手机上打出这个句子至少需要按多少下键盘。
输入格式

一行句子，只包含英文小写字母和空格，且不超过 200 个字符。
输出格式

一行一个整数，表示按键盘的总次数。
'''
s = input()
count = 0
for i in range(len(s)):
    if s[i] =="a" or s[i] == "d" or s[i] == "g" or s[i] == "j" or s[i] == "m" or s[i] == "p" or s[i] == "t" or s[i] == "w" or s[i] == " ":
        count += 1
    elif s[i] =="b" or s[i] == "e" or s[i] == "h" or s[i] == "k" or s[i] == "n" or s[i] == "q" or s[i] == "u" or s[i] == "x":
        count += 2
    elif s[i] =="c" or s[i] == "f" or s[i] == "i" or s[i] == "l" or s[i] == "o" or s[i] == "r" or s[i] == "v" or s[i] == "y":
        count += 3
    elif s[i] =="s" or s[i] == "z" :
        count += 4

print(count)