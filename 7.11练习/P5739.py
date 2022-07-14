'''题目描述
求 n!，也就是 1×2×3⋯×n。
挑战：尝试不使用循环语句（for、while）完成这个任务。
输入格式
第一行输入一个正整数 n。
输出格式
输出一个正整数，表示 n!。
'''
# n = int(input())
# jc = 1
# for i in range(1,n+1):
#     jc *= i
# print(jc)


def jiecheng(x,ans,n):
    ans *= x
    if x==n:
        print(ans)
        return
    jiecheng(x+1,ans,n)

n = int(input())
jiecheng(1,1,n)

