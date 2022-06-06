# https://leetcode.cn/problems/find-the-student-that-will-replace-the-chalk/

from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = 0
        for c in chalk:
            total += c
        valid_k = k % total
        for i, v in enumerate(chalk):
            if valid_k < v:
                return i
            valid_k -= v
        return -1


class Solution_II:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        if chalk[0] > k:
            return 0
        for i in range(1, n):
            chalk[i] += chalk[i - 1]
            if chalk[i] > k:
                return i

        k %= chalk[-1]
        left = 0
        right = n - 1
        k = k % chalk[-1]
        while left < right:
            mid = (left + right) // 2
            if chalk[mid] > k:
                right = mid
            else:
                left = mid + 1
        return right
