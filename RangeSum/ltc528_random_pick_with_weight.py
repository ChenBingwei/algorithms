# https://leetcode.cn/problems/random-pick-with-weight/

from random import randint
from itertools import accumulate
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = list(accumulate(w))
        self.total = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        x = randint(1, self.total)
        left = 0
        right = len(self.prefix_sum)
        while left < right:
            mid = (left + right) // 2
            if x <= self.prefix_sum[mid]:
                right = mid
            else:
                left = mid + 1
        return right
