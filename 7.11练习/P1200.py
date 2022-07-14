'''小组名和彗星名都以下列方式转换成一个数字：最终的数字就是名字中所有字母的积，其中 A 是 1,Z 是 26。例如，USACO小组就是 21×19×1×3×15=17955。如果小组的数字  mod 47等于彗星的数字  mod 47,你就得告诉这个小组需要准备好被带走！

写出一个程序，读入彗星名和小组名并算出用上面的方案能否将两个名字搭配起来，如果能搭配，就输出 GO，否则输出 STAY。小组名和彗星名均是没有空格或标点的一串大写字母（不超过 666 个字母）。
输入格式

第1行：一个长度为 1 到 6的大写字母串，表示彗星的名字。

第2行：一个长度为 1到 6的大写字母串，表示队伍的名字。
'''

a = input()
b = input()
ta = []
tb = []
for i in range(len(a)):
    ta.append(ord(a[i])-ord('A')+1)
for i in range(len(b)):
    tb.append(ord(b[i])-ord('A')+1)
# print(ta)
# print(tb)
ca = 1
cb = 1
for i in range(len(ta)):
    ca *= ta[i]
for i in range(len(tb)):
    cb *= tb[i]
ma = ca%47
mb = cb%47
if ma == mb:
    print('GO')
else:
    print('STAY')