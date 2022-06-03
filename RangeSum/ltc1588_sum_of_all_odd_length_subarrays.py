# https://leetcode.cn/problems/sum-of-all-odd-length-subarrays/

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        a = [0]
        prefix_sum = 0
        n = len(arr)
        for i in arr:
            prefix_sum += i
            a.append(prefix_sum)
        ans = 0
        for i in range(n + 1):
            length = 1
            while i + length < n + 1:
                ans += a[i + length] - a[i]
                length += 2
        return ans
