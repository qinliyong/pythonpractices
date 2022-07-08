'''题目描述
P 老师需要去商店买 n 支铅笔作为小朋友们参加 NOIP 的礼物。她发现商店一共有 3 种包装的铅笔，不同包装内的铅笔数量有可能不同，价格也有可能不同。
为了公平起见，P 老师决定只买同一种包装的铅笔。
商店不允许将铅笔的包装拆开，因此 P 老师可能需要购买超过 n 支铅笔才够给小朋友们发礼物。
现在 P 老师想知道，在商店每种包装的数量都足够的情况下，要买够至少 n 支铅笔最少需要花费多少钱。
输入格式
第一行包含一个正整数 n，表示需要的铅笔数量。
接下来三行，每行用 2 个正整数描述一种包装的铅笔：其中第 1 个整数表示这种包装内铅笔的数量，第 2 个整数表示这种包装的价格。
保证所有的 7 个数都是不超过 10000的正整数。
输出格式
1 个整数，表示 P 老师最少需要花费的钱。
'''
n = int(input())
cost = []
counta,pricea = map(int,input().split())
countb,priceb = map(int,input().split())
countc,pricec = map(int,input().split())
if n%counta == 0:
    numa = n//counta
else:
    numa = n//counta + 1

if n%countb == 0:
    numb = n//countb
else:
    numb = n//countb + 1

if n%countc == 0:
    numc = n//countc
else:
    numc = n//countc + 1
costa = numa*pricea
cost.append(costa)
costb = numb*priceb
cost.append(costb)
costc = numc*pricec
cost.append(costc)
print(min(cost))