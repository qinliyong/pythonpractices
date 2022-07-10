'''题目描述

八尾勇喜欢吃苹果。她今天吃掉了 x 个苹果。英语课上学到了 apple 这个词语，想用它来造句。
如果她吃了 1 个苹果，就输出 Today, I ate 1 apple.；如果她没有吃，那么就把 1 换成 0；如果她吃了不止一个苹果，别忘了 apple 这个单词后面要加上代表复数的 s。你能帮她完成这个句子吗？
输入格式

输入一行一个自然数 x，表示吃掉的苹果数。
输出格式

根据题目要求输出。
'''
x = int(input())
if x == 0:
    print("Today, I ate 0 apple.")
elif x == 1:
    print("Today, I ate 1 apple.")
elif x > 1:
    print("Today, I ate "+str(x)+" apples.")