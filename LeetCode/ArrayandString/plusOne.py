#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 1;

        """
        通过for循环range拿到从后往前遍历的列表的下标
        列表下标为0~len(digits)-1
        从(len(digits)-1)开始到(-1),步长为-1(即每次减1)
        """

        for i in range(len(digits)-1, -1, -1) :
            if digits[i]+flag == 10 :
                digits[i] = 0;
                flag = 1;
            else :
                digits[i] = digits[i]+flag;
                flag = 0;

        if flag == 1 :
            digits.insert(0, 1);
        return digits;
