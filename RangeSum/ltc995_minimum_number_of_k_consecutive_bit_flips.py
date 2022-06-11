from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(0, n):
            if nums[i] == 0:
                if i + k > n:
                    return -1
                for j in range(k):
                    nums[i + j] ^= 1
                ans += 1
        return ans


class Solution_II:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cnt = 0
        arr = [0] * (n + 1)
        for i in range(n):
            cnt += arr[i]
            if (nums[i] + cnt) % 2 == 0:
                if i + k > n:
                    return -1
                arr[i + 1] += 1
                arr[i + k] -= 1
                ans += 1
        return ans
