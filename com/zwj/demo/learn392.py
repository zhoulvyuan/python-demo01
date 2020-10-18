#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/27 15:49
# @Author : zhouwj
# @Version：V 0.1
# @File : learn392.py
# @desc : 判断子序列


def isSubsequence(self, s: str, t: str) -> bool:
    last_index = -1
    for subs in s:
        last_index = last_index + 1
        current_index = t.find(subs, last_index)
        if current_index == -1:
            return False
        else:
            last_index = current_index
    return True


if isSubsequence("", "abc", "ahbgdc"):
    print("成功")
else:
    print("失败")

