s = '666c61677b77656c636f6d65746f435446776f726c647d'

for i in range(0,len(s),2):
    print(chr(int(s[i:i+2],16)),end="")

print("------------------------------------------------")

flag = 'flag{welcometoCTFworld}'

for j in range(len(flag)):
    h = hex(ord(flag[j]))
    h1 = str(h)
    print(h1[2:],end="")