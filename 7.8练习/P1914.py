'''题目背景
某蒟蒻迷上了 “小书童”，有一天登陆时忘记密码了（他没绑定邮箱 or 手机），于是便把问题抛给了神犇你。
题目描述
蒟蒻虽然忘记密码，但他还记得密码是由一个字符串组成。密码是由原文字符串（由不超过 50 个小写字母组成）中每个字母向后移动 nnn 位形成的。
z 的下一个字母是 a，如此循环。他现在找到了移动前的原文字符串及 n，请你求出密码。
输入格式
第一行：n。第二行：未移动前的一串字母
输出格式
一行，是此蒟蒻的密码
'''
n = int(input())
enc_pass = input()
passwd = []
for i in range(len(enc_pass)):
    pa = (ord(enc_pass[i])+n)
    if pa > ord('z'):
        pa = pa-ord('z')+ord('a')-1
    pc = chr(pa)
    passwd.append(pc)

for j in range(len(passwd)):
    print(passwd[j],end="")

