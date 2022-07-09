n = int(input())
n1 = 0
n2 = 1
count = 2
if n == 0:
   print("0.00")
   exit()
if n == 1:
   print(n2,end="")
   print(".00")
   exit()
else:
   while count < (n+1):
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print(nth,end="")
print(".00")