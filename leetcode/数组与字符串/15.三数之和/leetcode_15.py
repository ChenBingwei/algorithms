from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for first in range(n):
            if first == 0 or nums[first] != nums[first - 1]:
                for second in range(first + 1, n):
                    if second == first + 1 or nums[second] != nums[second - 1]:
                        for third in range(second + 1, n):
                            if third == second + 1 or nums[third] != nums[third - 1]:
                                if nums[first] + nums[second] + nums[third] == 0:
                                    res.append([nums[first], nums[second], nums[third]])

        return res

    def three_sum_p(self, nums):
        n = len(nums)
        nums.sort()
        ans = []

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            third = n - 1
            target = - nums[first]
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


if __name__ == '__main__':
    test_list = [[-1, 0, 1, 2, -1, -4], [], [0]]
    func = Solution()
    for i in test_list:
        print(func.three_sum(i))
        print(func.three_sum_p(i))
        print("******************")
