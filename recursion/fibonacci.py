# -*- coding:utf-8 -*-

"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列、
因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

用递归生成斐波那契数列第N个数
"""


def fibonacci(n):
    if 0 < n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(8))


# 斐波那契数列生成器版本(性能高于递归)
def fib(n):
    a, b = 1, 1
    while n > 0:
        yield a
        n -= 1
        a, b = b, a+b


for i in fib(8):
    print(i)