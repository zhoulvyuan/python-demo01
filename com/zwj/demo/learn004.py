#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/8/3 15:33
# @Author : zhouwj
# @Version：V 0.1
# @File : learn004.py
# @desc : 寻找中位数
from typing import List


def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
    """
    列表排序合并，遍历列表1,列表2，将列表1、列表2合并到一个结果列表，对结果列表求中位数
    :param self:
    :param nums1:
    :param nums2:
    """
    idx1 = idx2 = 0
    len1 = len(nums1)
    len2 = len(nums2)
    result_list = []
    c_list = 1
    start_idx = 0
    end_idx = 0
    while idx1 < len1 or idx2 < len2:
        if idx1 < len1:
            num1 = nums1[idx1]
        else:
            result_list += nums2[idx2:len2]
            break

        if idx2 < len2:
            num2 = nums2[idx2]
        else:
            result_list += nums1[idx1:len1]
            break

        # 列表1的当前数据小于列表2的当前数据
        if num1 <= num2:
            start_idx = idx1
            idx1 += 1
            while idx1 < len1 and nums1[idx1] <= num2:
                idx1 += 1
            end_idx = idx1
            c_list = 1
        elif num1 > num2:
            start_idx = idx2
            idx2 += 1
            while idx2 < len2 and nums2[idx2] < num1:
                idx2 += 1
            end_idx = idx2
            c_list = 2
        result_list += nums1[start_idx:end_idx] if c_list == 1 else nums2[start_idx:end_idx]

    result_list_len = len(result_list)
    if result_list_len % 2 == 0:
        return (result_list[int(result_list_len/2)] + result_list[int(result_list_len/2) - 1])/2
    else:
        return result_list[int(result_list_len/2)]


def find_num(nums1, nums2, k):
    """
    采用二分法查找第k大值
    :param nums1:
    :param nums2:
    :param k:
    """
    m = len(nums1)
    n = len(nums2)
    if m < k:
        # 当k>m时，取列表nums1的最后以为与列表num2的第k位比较
        if nums1[m - 1] <= nums2[m + n - k]:
            return nums2[m + n - 2*k]
        else:
            return find_num(nums1, nums2)


def find_median_sorted_arrays2(self, nums1: List[int], nums2: List[int]) -> float:
    """
    根据中位数的定义可以通过对(m+n+1)/2与(m+n+2)/2的两个数进行取中位数，所以可以理解为
    :param self:
    :param nums1:
    :param nums2:
    """
    m = len(nums1)
    n = len(nums2)
    k1 = (m + n + 1) / 2 - 1
    k2 = (m + n + 2) / 2 - 1
    if k1 == k2:
        return find_num(nums1, nums2, k1)
    else:
        return (find_num(nums1, nums2, k1) + find_num(nums1, nums2, k2))/2

print(find_median_sorted_arrays("*", [], [3]))
