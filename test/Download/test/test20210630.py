# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 20:09
# @Author  : DL
# @Email   : 840806506@qq.com
# @File    : test20210630.py
# @Software: PyCharm
# @ Describe: --------------------
# #浮点数四舍五入取近似值
n = float(input("请输入n进行四舍五入:"))
nInt = int(n);
a = n - nInt;
if a>= 0.5:
    print(nInt+1);
else:
    print(nInt);
#
# #求int型正整数在内存中存储时1的个数
n = int(input("请输入n计算二进制中1的个数："))
n2 = bin(n)
print(n2.count("1"))


'''
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。
小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？
”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，
这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。
如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
'''
def func(a):
    sum = 0
    while a >= 3:
        sum += a // 3
        a = a // 3 + a % 3
    return sum + 1 if a == 2 else sum
while True:
    n = int(input("请输入空瓶子数量："))
    if n == 0: break
    print("可换的瓶子数：",func(n))

# 有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？
#斐波那契函数
while True:
    try:
        month = int(input("请输入经过几个月"));
        n = month - 1;
        def fun(n):
            if n < 2:
                return 1
            else:
                return fun(n-1)+fun(n-2)
        print(fun(n))
    except:
        break

# 输入一个表达式（用字符串表示），求这个表达式的值。
# 保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。
while True:
    try:
        sum = input("请输入四则表达式：").strip()
        sum=sum.replace("[", "(")
        sum=sum.replace("]", ")")
        sum=sum.replace("{", "(")
        sum=sum.replace("}", ")")
        print(int(eval(sum)))
    except:
        break


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#反转单向链表，后一个指针指向前一个结点，并且将表头指针指向最后一个结点
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        root = None
        while pHead:
            pHead.next,root,pHead = root,pHead,pHead.next
        return root


