# https://leetcode.cn/problems/subarray-sum-equals-k/

from itertools import accumulate
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = list(accumulate(nums))
        ans = 0
        mp = defaultdict(int)
        mp[0] = 1
        for s in sums:
            target = s - k
            if target in mp:
                ans += mp[target]
            mp[s] += 1
        return ans


class Solution_II:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        pre = ans = 0
        for num in nums:
            pre += num
            if pre == k:
                ans += 1
            if pre - k in mp:
                ans += mp[pre - k]
            mp[pre] += 1
        return ans
