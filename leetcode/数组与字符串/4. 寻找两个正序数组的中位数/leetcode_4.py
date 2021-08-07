from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        p1, p2, m, n = 0, 0, len(nums1), len(nums2)
        while True:
            if p1 == m:
                nums3 += nums2[p2:]
                break
            if p2 == n:
                nums3 += nums1[p1:]
                break
            if nums1[p1] < nums2[p2]:
                nums3.append(nums1[p1])
                p1 += 1
            else:
                nums3.append(nums2[p2])
                p2 += 1
        left_median = nums3[(m + n - 1) // 2]
        right_median = nums3[(m + n) // 2]
        ans = float((left_median + right_median) / 2)
        return ans


if __name__ == '__main__':
    res1 = Solution.findMedianSortedArrays([1, 3], [2])
    print(res1)
