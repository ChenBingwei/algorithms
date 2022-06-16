from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right + 1) // 2
            if self.count(nums, mid) >= k:
                right = mid - 1
            else:
                left = mid
        return right

    # 数对距离小于mid的个数
    def count(self, nums, target):
        n = len(nums)
        cnt = 0
        for i in range(n):
            left = 0
            right = i
            while left < right:
                mid = (left + right) // 2
                if nums[i] - nums[mid] >= target:
                    left = mid + 1
                else:
                    right = mid
            cnt += i - right
        return cnt
