# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 13:14
# @Author  : DL
# @Email   : 840806506@qq.com
# @File    : test20210701.py
# @Software: PyCharm
# @ Describe: --------------------
#杨辉三角
def triangle(max):
    tri = [1]
    pre = [1]
    n = 1
    while n <= max:
        yield tri
        for i in range(1,len(pre)):
            tri[i] = pre[i-1] + pre[i]
        tri.append(1)
        pre=tri[:]  #pre=tri表示将pre内存也指向tri，加[:]则指向新的内存地址
        n += 1
triangles = triangle(10)
for st in triangles:
    print(st)
#上面三个数是下面数之和，找第n行第一个偶数出现的位置。如果没有偶数，则输出-1
while True:
    try:
        a = int(input("请输入查询的行数："))
        l_0 = [[0 for i in range(2*a-1)] for i in range(a)]
        l_0[0][0] = 1
        for i in range(1,a):
            for j in range(len(l_0[0])):
                l_0[i][j] = l_0[i-1][j-2] + l_0[i-1][j-1] + l_0[i-1][j]
        for k in l_0[a-1]:
            if k % 2 == 0:
                print(l_0[a-1].index(k) + 1)
                break
        else:
            print('-1')
    except:
        break

'''
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。s
输入n，请输出n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
'''
while True:
    try:
        a = int(input("请输入值，计算含有多个完全数"))
        count = 0
        for i in range(1,a+1):
            sum = 0
            for j in range(1,i):
                if i % j == 0:
                    sum += j
            if sum == i:
                count += 1
        print(count)
    except:
        break


#最小公倍数
import math
a,b = map(int,input().split())
print(a*b/math.gcd(a, b))

#一个数的质子因数，所有数，可重复
n = int(input())
i = 2
while i < (n**0.5)+1:
    if n % i == 0:
        print(i,end=' ')
        n = n // i
        i = 2
    else:
        i += 1
print(n,end=' ')

'''
字符串排序
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
规则 3 ：非英文字母的其它字符保持原来的位置。
'''
while True:
    try:
        a = input()
        # res是最终返回的字符串的列表形式，char是提取的英文字母。
        res, char = [False] * len(a), []
        # 经过这个循环，把相应的非英文字母及其位置存储到了res中。并且把英文字母提取出来了。
        for i, v in enumerate(a):
            if v.isalpha():
                char.append(v)
            else:
                res[i] = v
        # 使用lambda表达式排序，暴力有效。
        char.sort(key=lambda c: c.lower())
        # 将char中对应的字符填到res中。
        for i, v in enumerate(res):
            if not v:
                res[i] = char[0]
                char.pop(0)
        print("".join(res))
    except:
        break

# 输出一个整数，表示输入字符串最后一个单词的长度。
while True:
    try:
        a = input()
        last = a.strip().split(" ")[-1]
        print(len(last))
    except:
        break