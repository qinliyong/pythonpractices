'''P5708 【深基2.习2】三角形面积
'''

a,b,c = map(float,input().split())
p =0.5*(a+b+c)
s = (p*(p-a)*(p-b)*(p-c))**0.5
print('%.1f'%s)