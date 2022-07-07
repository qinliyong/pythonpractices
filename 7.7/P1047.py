'''
题目描述
某校大门外长度为 l的马路上有一排树，每两棵相邻的树之间的间隔都是 1 米。我们可以把马路看成一个数轴，马路的一端在数轴 0 的位置，另一端在 l 的位置；
数轴上的每个整数点，即 0,1,2,…,l，都种有一棵树。
由于马路上有一些区域要用来建地铁。这些区域用它们在数轴上的起始点和终止点表示。已知任一区域的起始点和终止点的坐标都是整数，区域之间可能有重合的部分。
现在要把这些区域中的树（包括区域端点处的两棵树）移走。你的任务是计算将这些树都移走后，马路上还有多少棵树。
输入格式
第一行有两个整数，分别表示马路的长度 l 和区域的数目 m。
接下来 m 行，每行两个整数 u,v表示一个区域的起始点和终止点的坐标。
输出格式
输出一行一个整数，表示将这些树都移走后，马路上剩余的树木数量。
'''
getlandm = input().split()
l = int(getlandm[0])
m = int(getlandm[1])
#print(l,m)
tree = []
for i in range(l+1):
    tree.append(1)
#print(tree)
for j in range(m):
    point = input().split()
    start_point = int(point[0])
    end_point = int(point[1])
    for k in range(start_point,end_point+1):
        tree[k] = 0

num = tree.count(1)
print(num)