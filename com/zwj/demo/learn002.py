#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/31 15:52
# @Author : zhouwj
# @Version：V 0.1
# @File : learn002.py
# @desc : 两数相加
from typing import List


class ListNode:

    def __init__(self, x) -> None:
        self.val = x
        self.next = None


def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    result_node = current_node = None
    result = 0

    current_node1 = l1
    current_node2 = l2
    # 判断是否进位
    is_carry = False

    while True:
        if current_node1 is None and current_node2 is None:
            if is_carry:
                result = 1
                is_carry = False
            else:
                break
        else:
            data1 = data2 = 0
            if current_node1:
                data1 = current_node1.val
                current_node1 = current_node1.next

            if current_node2:
                data2 = current_node2.val
                current_node2 = current_node2.next

            result = data1 + data2
            if is_carry:
                result += 1
            if result > 9:
                result -= 10
                is_carry = True
            else:
                is_carry = False

        new_node = ListNode(result)
        if result_node:
            current_node.next = new_node
            current_node = current_node.next
        else:
            current_node = new_node
            result_node = current_node

    return result_node


def print_result(nodes: ListNode):
    if nodes:
        print(nodes.val)
        if nodes.next:
            print_result(nodes.next)


param1 = ListNode(5)
# param1.next = ListNode(5)
# param1.next.next = ListNode(3)
param2 = ListNode(7)
# param2.next = ListNode(6)
# param2.next.next = ListNode(4)
result_data = add_two_numbers("", param1, param2)
print_result(result_data)
