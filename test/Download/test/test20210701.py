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

#先输入n个整数,然后再输入值，进行去重排序后输出
while True:
    try:
        n = int(input())
        set1 = set({})
        for i in range(n):
            set1.add(int(input()))
        nums = list(set1)
        nums.sort()
        for i in nums:
            print(i)
    except:
        break

'''输入描述：
一个只包含小写英文字母和数字的字符串。
输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。'''
while True:
    try:
        str1 = input()#读取字符串
        str2 = list(str1)#转换list转存入str2
        str2 = set (str2)#去除重复项
        str2 = list(str2)#变回list
        a=[]
        for i in range (len(str2)):#计算每一项个数
            num =str1.count(str2[i])
            a.append((ord(str2[i]),num))#以（asc码，count个数）的形式添加入a里（a为list）用ord()转换为ASCII码
        a.sort(key=lambda x:x[0])#先ASCII 码升序排列
        a.sort(key=lambda x:x[1],reverse=True)#再出现次数降序排列，遇到相同的排序会预设按输入次序也就是上行ASCII的sort排序顺序
        str3=""
        for i in range (len(a)):
            str3 = str3+str(chr(a[i][0])) #用chr（）换回字母数字，打印结果
        print(str3)
    except:
        break
'''输入描述：
连续输入字符串(输入多次,每个字符串长度小于100)
输出描述：
输出到长度为8的新字符串数组'''
while True:
    try:
        s = input()
        while len(s) >= 8:
            print(s[:8])
            s = s[8:]
        if len(s) > 0:
            print(s+'0'*(8-len(s)))
    except:
        break

'''描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
输入描述：
先输入键值对的个数
然后输入成对的index和value值，以空格隔开
输出描述：
输出合并后的键值对（多行）'''
# 读取行数num
num = int(input())
# 通过字典存储索引和数值
dct = {}
# 读取接下来的num行
for i in range(num):
    # 索引和数值
    idx, val = [int(j) for j in input().split()]
    # 如果元素未出现，默认值为0，否则累加
    dct[idx] = dct.get(idx, 0) + val

# 按key升序排列
for key in sorted(dct.keys()):
    print(key, dct[key])


'''
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出。
本题含有多组输入数据。
'''
while True:
    try:
        m = int(input())
        s = []
        for i in range(1,m**3):
            if i % 2 != 0:   #先取出所有奇数
                s.append(i)
                if m **3 == sum(s[-m:]):   #得到的奇数和都是m个数
                    s = s[-m:]
                    break
        result = str(s[0])   #取得到第一个奇数，之后进行遍历
        for k in range(1,m):
            result += '+'+str(s[k])
        print(result)
    except:
        break