'''
水仙花数是指：百位数的3次方+十位数的3次方+个位数的3次方=数值本身
输出所有3位水仙花数
'''
for i in range(100,1000):
    # a = i//100
    # b = i%100//10
    # c = i%10
    # if a**3+b**3+c**3 == i :
    #     print(i)
    a,b,c = str(i)
    if int(a)**3+int(b)**3+int(c)**3 == i :
        print(i)

