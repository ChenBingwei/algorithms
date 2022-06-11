class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        prefix_sums = [0]
        for i in range(n):
            prefix_sums.append(prefix_sums[i] + ord(s[i]) - ord("0"))

        ans = n
        for i in range(1, n + 1):
            # i左边1的个数
            l = prefix_sums[i - 1]
            # i右边0的个数
            r = (n - i) - (prefix_sums[n] - prefix_sums[i])
            ans = min(ans, l + r)
        return ans
