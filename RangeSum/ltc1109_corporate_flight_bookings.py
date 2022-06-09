# https://leetcode.cn/problems/corporate-flight-bookings/
from collections import defaultdict
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        up_dict = defaultdict(int)
        for first, last, seat in bookings:
            up_dict[first] += seat
            up_dict[last + 1] -= seat
        ans = []
        s = 0
        for i in range(1, n + 1):
            if i in up_dict:
                s += up_dict[i]
            ans.append(s)
        return ans


class Solution_II:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        for first, last, seat in bookings:
            nums[first - 1] += seat
            if last < n:
                nums[last] -= seat
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums
