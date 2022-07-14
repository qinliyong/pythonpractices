'''
假设a='CaptureTheFlag'
1.取出前7个字符 Capture
2.取出后4个字符 Flag
3.取出第8-10个字符 The
4.取出第8之后的字符 TheFlag
5.反转字符串
'''
a='CaptureTheFlag'
print(a[0:7])
print(a[-4::])
print(a[7:10])
print(a[7:])
print(a[::-1])