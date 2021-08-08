class Solution:

    def valid_palindrome(self, s: str) -> bool:
        # if left > right:
        #     return False
        # if right - left + 1 < 2:
        #     return True
        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        return s == s[-1::-1]

    # function 1
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        begin, maxlen = 0, 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if j - i + 1 > maxlen and self.valid_palindrome(s[i:j + 1]):
                    begin = i
                    maxlen = j - i + 1
        return s[begin:begin + maxlen]

    # function 2
    def longestPalindrome_p(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        begin, maxlen = 0, 1
        for i in range(n - 1):
            oddlen = self.expand_aroud_center(s, i, i)
            eventlen = self.expand_aroud_center(s, i, i + 1)
            cur_len = max(oddlen, eventlen)
            if maxlen < cur_len:
                maxlen = cur_len
                # odd: begin = i - (maxlen - 1) / 2
                # even: begin = i - (maxlen - 2) / 2
                begin = i - (maxlen - 1) // 2

        return s[begin:begin + maxlen]

    def expand_aroud_center(self, s: str, left: int, right: int) -> int:
        n = len(s)
        while left >= 0 and right < n:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        # 退出循环时，刚好满足s[left] != s[right]，left和right均进行了一次加减运算，因此
        # 长度为 right - left + 1 -2
        return right - left - 1

    # function 3：动态规划
    # dp[i][j]表示子串s[i..j]是否为回文子串
    # 状态转移方程即为 dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
    # 边界条件为 j - 1 - (i + 1) + 1 < 2,整理得 j - i < 3 等价于 j - i + 1 < 4
    # 表示s[i..j]长度为2或者3时，不用检查是否为回文子串
    # 初始化： dp[i][i] = True
    # 输出： 得到一个状态值为true的时候，记录起始位置和长度，最后再截取
    def longestPalindrome_pp(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        begin, maxlen = 0, 1
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for j in range(n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    begin = i
        return s[begin:begin + maxlen]


if __name__ == '__main__':
    test_str = ["adbab", "cbbd", "a", "ac"]
    func = Solution()
    for i in test_str:
        print(
            func.longestPalindrome(i),
            func.longestPalindrome_p(i),
            func.longestPalindrome_pp(i)
        )
