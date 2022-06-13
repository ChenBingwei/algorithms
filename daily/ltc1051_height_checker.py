from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        compare = heights.copy()
        n = len(compare)
        for i in range(n):
            for j in range(i + 1, n):
                if compare[i] > compare[j]:
                    compare[i], compare[j] = compare[j], compare[i]
        ans = 0
        for i in range(n):
            if heights[i] != compare[i]:
                ans += 1
        return ans


class Solution_II:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        compare = sorted(heights)
        ans = 0
        for i in range(n):
            if heights[i] != compare[i]:
                ans += 1
        return ans


class Solution_III:
    def heightChecker(self, heights: List[int]) -> int:
        m = max(heights)
        cnt = [0] * (m + 1)

        for h in heights:
            cnt[h] += 1

        idx = ans = 0
        for i in range(1, m + 1):
            for j in range(cnt[i]):
                if heights[idx] != i:
                    ans += 1
                idx += 1

        return ans
