from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = 0
        for i in matchsticks:
            total_length += i
        if total_length % 4 != 0:
            return False
        matchsticks.sort(reverse=True)

        side_length = total_length / 4

        edges = [0] * 4

        def dfs(idx):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= side_length and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks[idx]
            return False

        return dfs(0)
