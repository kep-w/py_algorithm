# -*- coding:utf-8 -*-

"""
冒泡排序，从左到右依次比较列表相邻的两个数，如果前边的比后边的大，那么交换顺序，经过一次排序后，最大的数就到了末尾
时间复杂度是O(n2)
"""


def bubble(lst):
    for i in range(len(lst)):
        flag = False
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                flag = True
        if not flag:
            return lst
    return lst


lst = [3, 1, 2, 4, 6, 5, 7, 9, 0, 8]
lst2 = [0, 1, 2, 3, 4, 5, 6, 9, 8, 7]
print(bubble(lst2))