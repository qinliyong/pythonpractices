'''题目描述

输入一个小写字母，输出其对应的大写字母。例如输入 q[回车] 时，会输出 Q。
'''
# s = input()
# print(s.upper())
s = input()
change = ord('A')-ord('a')
print(chr(ord(s)+change))