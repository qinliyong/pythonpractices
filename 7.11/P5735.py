'''题目描述
给出平面坐标上不在一条直线上三个点坐标 (x1,y1),(x2,y2),(x3,y3)，坐标值是实数，且绝对值不超过 100.00，求围成的三角形周长。保留两位小数。
对于平面上的两个点 (x1,y1),(x2,y2)，则这两个点之间的距离 dis=sqrt{(x2-x1)^2+(y2-y1)^2}

输入格式
输入三行，第 i 行表示坐标 (xi,yi)，以一个空格隔开。
输出格式
输出一个两位小数，表示由这三个坐标围成的三角形的周长。
'''
def dis(x1,y1,x2,y2):
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    return d

a = input().split()
b = input().split()
c = input().split()
ax = float(a[0])
ay = float(a[1])
bx = float(b[0])
by = float(b[1])
cx = float(c[0])
cy = float(c[1])

dis_ab = dis(ax,ay,bx,by)
dis_ac = dis(ax,ay,cx,cy)
dis_bc = dis(bx,by,cx,cy)

l = dis_ab+dis_ac+dis_bc
print("%.2f"%l)
