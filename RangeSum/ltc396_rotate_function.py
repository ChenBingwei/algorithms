# https://leetcode.cn/problems/rotate-function/

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        n = len(nums)
        f = [0 for _ in range(n)]
        for i, v in enumerate(nums):
            f[0] += i * v
        for i in range(1, n):
            f[i] = f[i - 1] + nums_sum - n * nums[n - i]
        return max(f)
