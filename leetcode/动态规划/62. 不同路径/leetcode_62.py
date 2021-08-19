class Solution:
    @staticmethod
    def uniquePaths(m, n):
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j - 1]
        return dp[m - 1][n - 1]

    @staticmethod
    def uniquePaths_p(m, n):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    test_list = [(3, 7), (3, 2), (7, 3)]
    for i, j in test_list:
        print(
            Solution.uniquePaths(i, j),
            Solution.uniquePaths_p(i, j)
        )
