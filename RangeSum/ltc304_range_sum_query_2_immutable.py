# https://leetcode.cn/problems/range-sum-query-2d-immutable/

from typing import List


class NumMatrix_a:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.prefix_sum = [[0 for _ in range(n)] for _ in range(m)]
        for k, v in enumerate(matrix):
            tmp_predix_sum = 0
            for k2, v2 in enumerate(v):
                tmp_predix_sum += v2
                self.prefix_sum[k][k2] = tmp_predix_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.prefix_sum[i][col2] - self.prefix_sum[i][col1] + self.matrix[i][col1]
        return ans


class NumMatrix_b:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix_sum = [[0 for _ in range(n + 1)] for _ in range(m)]
        for k, v in enumerate(matrix):
            tmp_predix_sum = 0
            for k2, v2 in enumerate(v):
                tmp_predix_sum += v2
                self.prefix_sum[k][k2 + 1] = tmp_predix_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.prefix_sum[i][col2 + 1] - self.prefix_sum[i][col1]
        return ans


class NumMatrix_c:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix_sum_2d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix_sum_2d[i][j] = matrix[i - 1][j - 1] + \
                                           self.prefix_sum_2d[i - 1][j] + \
                                           self.prefix_sum_2d[i][j - 1] - \
                                           self.prefix_sum_2d[i - 1][j - 1]

        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum_2d[row2 + 1][col2 + 1] - \
               self.prefix_sum_2d[row2 + 1][col1] - \
               self.prefix_sum_2d[row1][col2 + 1] + \
               self.prefix_sum_2d[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
