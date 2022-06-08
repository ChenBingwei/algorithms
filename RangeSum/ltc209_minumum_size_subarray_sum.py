# https://leetcode.cn/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sums = 0
        left = 0
        right = 0
        ans = n + 1
        while right < n:
            sums += nums[right]
            while sums >= target:
                ans = min(ans, right - left + 1)
                sums -= nums[left]
                left += 1
            right += 1
        return 0 if ans == n + 1 else ans
