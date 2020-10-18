#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/8/2 15:18
# @Author : zhouwj
# @Version：V 0.1
# @File : learn003.py
# @desc : 无重复字符的最长字串


def length_of_longest_substring(self, s: str) -> int:
    """
    从字符串首部开始遍历拼接，每一次拼接时做如下操作：

    1.校验当前拼接的字符是否存在，若已存在则截取当前字符第一次出现的位置之后的元素，否则取拼接字符串长度

    2.校验拼接字符串长度是否大于收集的最大字串长度，若大于则替换
    :param self:
    :param s:
    :return:
    """
    max_len = 0
    c_str = []
    for c_s in s:
        c_str.append(c_s)
        if c_str.count(c_s) > 1:
            c_str = c_str[c_str.index(c_s) + 1:]
        else:
            max_len = max(max_len, len(c_str))
    return max_len


def length_of_longest_substring2(self, s: str) -> int:
    """
    从字符串首部开始遍历，将字符出现的位置记录在字典中，并做如下操作：

    校验当前记录的字符是否存在，若已存在且字符传位置在起始标志位之后，则重新计算起始标志位、字符子串长度
    :param self:
    :param s:
    :return:
    """
    max_len = 0
    c_start = 0
    mark = {}
    for index, c_s in enumerate(s):
        if c_s in mark and mark[c_s] >= c_start:
            c_len = index - c_start
            max_len = max(c_len, max_len)
            c_start = mark[c_s] + 1
        mark[c_s] = index
    else:
        c_str_len = len(s) - c_start
        max_len = max(c_str_len, max_len)

    return max_len


print(length_of_longest_substring2("*", "abcabcdeacderfg"))

