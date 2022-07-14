'''题目描述
猪猪 Hanke 特别喜欢吃烤鸡（本是同畜牲，相煎何太急！）Hanke 吃鸡很特别，为什么特别呢？
因为他有 10 种配料（芥末、孜然等），每种配料可以放 1 到 3 克，任意烤鸡的美味程度为所有配料质量之和。
现在， Hanke 想要知道，如果给你一个美味程度 n ，请输出这 10 种配料的所有搭配方案。
输入格式
一个正整数 n，表示美味程度。
输出格式
第一行，方案总数。
第二行至结束，10 个数，表示每种配料所放的质量，按字典序排列。
如果没有符合要求的方法，就只要在第一行输出一个 0。
'''
n = int(input())
if n<10 or n>30:
    print(0)
    exit()
count = 0
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            for d in range(1,4):
                for e in range(1,4):
                    for f in range(1,4):
                        for g in range(1,4):
                            for h in range(1,4):
                                for i in range(1,4):
                                    for j in range(1,4):
                                        if a+b+c+d+e+f+g+h+i+j == n :
                                            count +=1
print(count)
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            for d in range(1,4):
                for e in range(1,4):
                    for f in range(1,4):
                        for g in range(1,4):
                            for h in range(1,4):
                                for i in range(1,4):
                                    for j in range(1,4):
                                        if a+b+c+d+e+f+g+h+i+j == n :
                                            print(a,b,c,d,e,f,g,h,i,j)