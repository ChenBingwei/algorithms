# https://leetcode.cn/problems/consecutive-numbers-sum/
from math import sqrt


class Solution_a:
    def consecutiveNumbersSum(self, n: int) -> int:
        left = 1
        right = 1
        get_sum = 1
        if n == 1:
            return 1
        ans = 0
        while right < n:
            while get_sum < n:
                right += 1
                get_sum += right
            while get_sum > n:
                get_sum -= left
                left += 1
            if get_sum == n:
                ans += 1
                get_sum -= left
                left += 1
        return ans


# n 是否可以表示成 k 个连续正整数之和的方法：
# 如果 k 是奇数，则当 n 可以被 k 整除时，正整数 n 可以表示成 k 个连续正整数之和；
# 如果 k 是偶数，则当 n 不可以被 k 整除且 2n 可以被 k 整除时，正整数 n 可以表示成 k 个连续正整数之和。
class Solution_b:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n: int, k: int) -> bool:
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans


class Solution_c:
    def consecutiveNumbersSum(self, n: int) -> int:
        m = int(sqrt(2 * n))
        ans = 0
        for i in range(1,m+1):
            # (2x + k - 1)k = 2n
            if (2*n) % i != 0:
                continue
            if ((2*n) / i - (i-1)) % 2 == 0:
                ans += 1
        return ans