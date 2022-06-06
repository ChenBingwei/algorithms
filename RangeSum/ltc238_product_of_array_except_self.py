# https://leetcode.cn/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product_list = [1 for _ in range(n)]
        suffix_product_list = [1 for _ in range(n)]
        for i in range(1, n):
            # not include i
            prefix_product_list[i] = prefix_product_list[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            # not include i
            suffix_product_list[i] = suffix_product_list[i + 1] * nums[i + 1]
        ans = []
        for i in range(n):
            t = prefix_product_list[i] * suffix_product_list[i]
            ans.append(t)
        return ans


class Solution_II:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        r = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * r
            r = r * nums[i]

        return ans
