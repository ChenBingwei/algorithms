import sys
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

    @staticmethod
    def findMedianSortedArrays_p(nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left = 0
        right = m
        while left < right:
            i = left + (right - left + 1) // 2
            j = total_left - i
            if nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                left = i
        i_final = left
        j_final = total_left - i_final

        nums1_left_max = -sys.maxsize if i_final == 0 else nums1[i_final - 1]
        nums1_right_min = sys.maxsize if i_final == m else nums1[i_final]
        nums2_left_max = -sys.maxsize if j_final == 0 else nums2[j_final - 1]
        nums2_right_min = sys.maxsize if j_final == n else nums2[j_final]

        if (m + n) % 2 == 1:
            return float(max(nums1_left_max, nums2_left_max))
        else:
            return float(max(nums1_left_max, nums2_left_max) + min(nums2_right_min, nums1_right_min)) / 2


if __name__ == '__main__':
    res1 = Solution.findMedianSortedArrays([1, 3], [2])
    print(res1)
    res2 = Solution.findMedianSortedArrays_p([], [1])
    print(res2)
