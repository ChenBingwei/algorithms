# https://leetcode.cn/problems/koko-eating-bananas/

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.valid_speed(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def valid_speed(self, piles, h, speed):
        if speed == 0:
            return False
        for pile in piles:
            h -= -1 * (-pile // speed)
            if h < 0:
                return False
        return True
