'''题目描述
You will be given three integers A, B and C. The numbers will not be given in that exact order, but we do know that A is less than B and B less than C. In order to make for a more pleasant viewing, we want to rearrange them in the given order.
输入格式
The first line contains three positive integers A, B and C, not necessarily in that order. All three numbers will be less than or equal to 100. The second line contains three uppercase letters 'A', 'B' and 'C' (with no spaces between them) representing the desired order.
输出格式
Output the A, B and C in the desired order on a single line, separated by single spaces.
'''
abc = input().split()
shunxu = input().strip()
for i in range(len(abc)):
    abc[i] = int(abc[i])
abc.sort()
a = abc[0]
b = abc[1]
c = abc[2]
if shunxu == 'ABC':
    print(a,b,c)
elif shunxu == 'ACB':
    print(a,c,b)
elif shunxu == 'BAC':
    print(b,a,c)
elif shunxu == 'BCA':
    print(b,c,a)
elif shunxu == 'CAB':
    print(c,a,b)
elif shunxu == 'CBA':
    print(c,b,a)