'''题目描述
给出三条线段 a,b,c 的长度，均是不大于 10000 的整数。打算把这三条线段拼成一个三角形，它可以是什么三角形呢？
    如果三条线段不能组成一个三角形，输出Not triangle；
    如果是直角三角形，输出Right triangle；
    如果是锐角三角形，输出Acute triangle；
    如果是钝角三角形，输出Obtuse triangle；
    如果是等腰三角形，输出Isosceles triangle；
    如果是等边三角形，输出Equilateral triangle。
如果这个三角形符合以上多个条件，请按以上顺序分别输出，并用换行符隔开。
'''
'''当两短边的平方和大于一长边的平方，说明是锐角三角形。
当两短边的平方和等于一长边的平方，说明是直角三角形。
当两短边的平方和小于一长边的平方，说明是钝角三角形。
'''
abc = input().split()
for i in range(len(abc)):
    abc[i] = int(abc[i])
abc.sort()
a = abc[0]
b = abc[1]
c = abc[2]
if (a+b) <= c :
    print("Not triangle")
    exit()
t1 = a*a+b*b
t2 = c*c
if t1>t2:
    print("Acute triangle")
elif t1==t2:
    print("Right triangle")
elif t1<t2:
    print("Obtuse triangle")

if a==b or b==c or a==c :
    print("Isosceles triangle")
if a==b==c:
    print("Equilateral triangle")
