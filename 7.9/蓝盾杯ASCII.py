'''
hint:需要将每一组二进制数最高位的1去掉
'''
s = 'd4e8e5a0f1f5e9e3eba0e2f2eff7eea0e6eff8a0eaf5edf0a0eff6e5f2a0f4e8e5a0ece1faf9a0e4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0c2c4c3d4c6fbd9b0f5dfe1f2e5dff3ede1f2b7fd'

for i in range(0,len(s),2):
    print(chr(int(s[i:i+2],16)-128),end="")