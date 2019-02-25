# -*- coding:utf-8 -*-

"""
把列表分为有序区和无序区两个部分。
最初有序区只有一个元素。然后每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空。
时间复杂度O(n2)
"""


def insert_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i -1
        while j >= 0:
            if lst[j] > temp:
                lst[j+1], lst[j] = lst[j], temp
            j -= 1
    return lst

lst = [2,4,3,1,6,5]
print(insert_sort(lst))
