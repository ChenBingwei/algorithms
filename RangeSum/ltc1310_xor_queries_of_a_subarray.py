from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0]
        n = len(arr)
        for i in range(n):
            prefix_xor.append(prefix_xor[i] ^ arr[i])
        ans = []
        for x, y in queries:
            ans.append(prefix_xor[x] ^ prefix_xor[y + 1])
        return ans
