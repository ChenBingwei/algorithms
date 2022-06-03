# https://leetcode.cn/problems/friends-of-appropriate-ages/
from typing import List


class Solution_a:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        left = 0
        right = 0
        ans = 0
        for i in range(n):
            if ages[i] < 15:
                continue
            while ages[left] <= 0.5 * ages[i] + 7:
                left += 1
            while right + 1 < n and ages[right + 1] <= ages[i]:
                right += 1
            ans += right - left
        return ans


class Solution_b:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        left = right = ans = 0
        for i in range(n):
            while left < i and not self.check(ages[i], ages[left]):
                left += 1
            if right < i:
                right = i
            while right + 1 < n and self.check(ages[i], ages[right + 1]):
                right += 1
            ans += right - left
        return ans

    def check(self, x, y):
        if y <= 0.5 * x + 7:
            return False
        if y > x:
            return False
        if y > 100 and x < 100:
            return False
        return True


class Solution_c:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        prefix_sum = [0] * 121
        for i in range(1, 121):
            prefix_sum[i] = prefix_sum[i - 1] + cnt[i]

        ans = 0
        for i in range(15, 121):
            if cnt[i] > 0:
                ans += cnt[i] * (prefix_sum[i] - prefix_sum[int(0.5 * i + 7)] - 1)
        return ans
