#! /usr/bin/env python
# -*- encoding : UTF-8 -*-

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        将nums列表的所有元素赋值给另外一个列表，再进行排序
        列表最后的一个元素就是整个列表的最大值
        只需求最大值是否是大于次大值的2倍
        即是查找数组中的最大元素是否至少是数组中每个其他元素的两倍
        """
        duplicate = nums[:];

        duplicate.sort();

        if len(duplicate) == 1 :
            return 0;

        if duplicate[-1] < (duplicate[-2]*2) :
            return -1;
        else :
            return nums.index(duplicate[-1]);
