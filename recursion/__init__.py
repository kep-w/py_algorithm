# -*-coding:utf-8 -*-

"""
递归：
    1.函数本身调用自己
    2.有条件控制出口，避免出现无线递归（递归过深会导致栈溢出）

    关于递归次数，Python中有个限制，可以通过sys模块来修改
    import sys
    sys.setrecursionlimit(10000)
"""