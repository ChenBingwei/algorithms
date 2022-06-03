# https://leetcode.cn/problems/image-smoother/

from itertools import product
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        prefix_sum_2d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i, j in product(range(1, m + 1), range(1, n + 1)):
            prefix_sum_2d[i][j] = prefix_sum_2d[i][j - 1] + \
                                  prefix_sum_2d[i - 1][j] - \
                                  prefix_sum_2d[i - 1][j - 1] + \
                                  img[i - 1][j - 1]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in product(range(m), range(n)):
            row1 = max(0, i - 1)
            row2 = min(m - 1, i + 1)
            col1 = max(0, j - 1)
            col2 = min(n - 1, j + 1)
            count = (row2 - row1 + 1) * (col2 - col1 + 1)
            total = prefix_sum_2d[row2 + 1][col2 + 1] - \
                    prefix_sum_2d[row2 + 1][col1] - \
                    prefix_sum_2d[row1][col2 + 1] + \
                    prefix_sum_2d[row1][col1]
            ans[i][j] = total // count
        return ans
