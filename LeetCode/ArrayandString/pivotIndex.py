#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = sum(nums);
        left = 0;
        """
        :enumerate函数返回的是索引和键值
        :left为当前key项的和
        """
        for key, value in enumerate(nums):
            left += value;
            if left*2 - value == ret:
                return key;
        return -1;
