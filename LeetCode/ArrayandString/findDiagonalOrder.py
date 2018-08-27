#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        """
        判断w和h的范围是在边界之内还是之外，做进一步处理
        初始对角线方向为右上方(偏移量:行-1, 列+1), 遇到边界时转向左下方(偏移量:行+1, 列-1)
        向右上方移动遇到上边界时, 若未达到右边界, 则向右移动(偏移量:行+0, 列+1),否则向下移动（偏移量：行+1，列+0）
        向左下方移动遇到左边界时, 若未达到下边界, 则向下移动(偏移量:行+1, 列+0), 否则向右移动(偏移量:行+0, 列+1).
        """

        if not matrix : return [];

        returned = [];
        i, j, k = 0, 0, 1;
        matrixRowSize, matrixColSize = len(matrix), len(matrix[0]);

        for x in range(matrixRowSize*matrixColSize) :
            returned.append(matrix[i][j]);
            if k > 0 :
                w, h = i - 1, j + 1;
            else :
                w, h = i + 1, j - 1;
            if 0 <= w < matrixRowSize and 0 <= h < matrixColSize :
                i, j = w, h;
            else:
                if k > 0 :
                    if j + 1 < matrixColSize :
                        j += 1;
                    else :
                        i += 1;
                else :
                    if i + 1 < matrixRowSize :
                        i += 1;
                    else :
                        j += 1
                k *= -1;
        return returned;
