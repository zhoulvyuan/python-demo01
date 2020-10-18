#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/9/19 10:40
# @Author : zhouwj
# @Version：V 0.1
# @File : huanjiu.py
# @desc : 换酒问题，N个酒瓶可以换一瓶酒，有M瓶酒，共可以和多少瓶

def huan_jiu(M, N):
    dreaked = M
    empty = dreaked
    while int(empty/N) > 0:
        dreaked += int(empty/N)
        empty = int(empty/N) + empty % N
    return dreaked


print(huan_jiu(9, 1))
