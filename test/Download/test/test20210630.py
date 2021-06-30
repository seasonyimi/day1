# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 20:09
# @Author  : DL
# @Email   : 840806506@qq.com
# @File    : test20210630.py
# @Software: PyCharm
# @ Describe: --------------------
#浮点数四舍五入取近似值
n = float(input("请输入n:"))
nInt = int(n);
a = n - nInt;
if a>= 0.5:
    print(nInt+1);
else:
    print(nInt);

#求int型正整数在内存中存储时1的个数
n = int(input())
n2 = bin(n)
print(n2.count("1"))