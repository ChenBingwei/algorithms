# https://leetcode.cn/problems/range-sum-query-immutable/
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_list = [0]
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            self.prefix_sum_list.append(prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum_list[right+1] - self.prefix_sum_list[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
