from typing import List


class Solution_A:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum_list = [0]
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefix_sum_list.append(prefix_sum)
        prefix_sum_list.append(0)
        n = len(prefix_sum_list)

        for i in range(1, n - 1):
            if prefix_sum_list[i - 1] == prefix_sum_list[n - 2] - prefix_sum_list[i]:
                return i - 1
        return -1


class Solution_B:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        haft_sum = 0
        for i in range(len(nums)):
            if haft_sum * 2 + nums[i] == total:
                return i
            haft_sum += nums[i]
        return -1
