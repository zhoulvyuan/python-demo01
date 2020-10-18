#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/27 16:52
# @Author : zhouwj
# @Version：V 0.1
# @File : learn001.py
# @desc : 两数之和
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    排序首位遍历相加

    1.对原始数据进行排序
    2.对排序后的列表遍历取第一个数，从列表第一个数开始遍历
    3.对排序后的列表遍历取第二个数，从列表最后一个数开始遍历
    4.对两个数求和，若两数之和等于目标值，则返回两个数的原始下标；若两数之和小于目标值，则重新获取第一个数；若两数之和大于目标值，则重新获取第二个数
    :param self:
    :param nums:
    :param target:
    :return:
    """
    first_index = 0
    org_list = []
    for current_index, num in nums:
        org_list.append({"index": current_index, "num": num})
        current_index += 1
    # 按照升序将列表排序
    org_list.sort(key=lambda data: data["num"], reverse=False)

    while first_index < len(nums):
        first_num = org_list[first_index]
        last_index = len(nums) - 1
        while last_index > first_index:
            first_num_data = first_num["num"]
            last_num_data = org_list[last_index]["num"]
            if first_num_data + last_num_data == target:
                result = [first_num["index"], org_list[last_index]["index"]]
                result.sort()
                return result
            elif first_num_data + last_num_data < target:
                break
            else:
                last_index -= 1
        first_index += 1


def twoSum2(self, nums: List[int], target: int) -> List[int]:
    """
    hash遍历查找

    1.将元组封装成字典,字典key为元组内容,value为元组下标,对于重复的元组,value采用元组的形式存放所有的下标
    2.对字典遍历,对字段的key与target做差,通过字典的hash判断差值是否是字典的key
    :param self:
    :param nums:
    :param target:
    :return:
    """
    org_list = {}
    for current_index, value in enumerate(nums):
        if org_list.__contains__(value):
            org_list[value] = [org_list[value], current_index]
        else:
            org_list[nums[current_index]] = current_index
    for key in org_list:
        last_num = target - key
        if last_num == key and type(org_list[key]) == list:
            result = org_list[last_num]
            result.sort()
            return result
        elif last_num == key:
            continue
        if org_list.__contains__(last_num):
            result = [org_list[key], org_list[last_num]]
            result.sort()
            return result


def twoSum3(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


print(twoSum3([3, 3, 4, 7], 6))

