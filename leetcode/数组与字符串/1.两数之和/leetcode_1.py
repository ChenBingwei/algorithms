from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        item_dict = {}
        for k, v in enumerate(nums):
            if target - v in item_dict:
                return [item_dict[target - v], k]
            item_dict[v] = k
        return []


if __name__ == '__main__':
    # res1 = Solution.twoSum([2,7,11,15], 9)
    res1 = Solution.twoSum([3, 2, 4], 6)
    print(res1)
