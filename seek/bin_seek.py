# -*-coding:utf-8 -*-

"""
所谓二分查找就是一分为二的查找，看目标值在左边一半还是右边一半，然后替换左端点或者右端点，继续判断
二分查找前提是有序序列
"""


def bin_search(lst, val):
    l, r = 0, len(lst)-1
    while l <= r:
        m = (l + r) // 2
        if lst[m] == val:
            return m
        elif lst[m] > val:
            r = m - 1
        else:
            l = m + 1


print(bin_search(range(5), 4))