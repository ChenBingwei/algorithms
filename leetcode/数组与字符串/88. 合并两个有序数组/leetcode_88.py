from typing import List


class Solution:

    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort(reverse=False)

    @staticmethod
    def merge_p(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        p1, p2 = 0, 0
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
        nums1[:] = nums3

    @staticmethod
    def merge_pp(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, tail = m - 1, n - 1, m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                cur = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                cur = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                cur = nums1[p1]
                p1 -= 1
            else:
                cur = nums2[p2]
                p2 -= 1
            nums1[tail] = cur
            tail -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    Solution.merge_p(nums1, m, nums2, n)
    print(nums1)
