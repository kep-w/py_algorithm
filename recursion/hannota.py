# -*- coding:utf-8 -*-

"""
三根相邻的柱子，标号为A,B,C，A柱子上从下到上按金字塔状叠放着n个不同大小的圆盘；
现在把所有盘子一个一个移动到柱子C上，并且每次移动同一根柱子上都不能出现大盘子在小盘子上方；

分析：
    将问题分解，如果只有一个盘子，可以直接A--》C
    那么当有N个时，可以分解为 1 + （N-1）
        先将N-1移动到B，
        然后最后一个移动到C，
        再将N-1移动到C
"""


SUM = 0

def hannota(n, a, b, c):
    global SUM
    if n == 1:
        SUM += 1
        print('\t', a, "-->", c)
        return
    hannota(n-1, a, c, b)
    print('\t', a, '-->', c)
    SUM += 1
    hannota(n-1, b, a, c)

print('盘子移动过程：')
hannota(3, 'A', 'B', 'C')
print('总共需要移动次数为：', SUM)

