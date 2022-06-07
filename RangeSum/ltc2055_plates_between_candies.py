# https://leetcode.cn/problems/plates-between-candles/

from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum = 0
        prefix_sum_dict = {}
        # 每一个下标右边第一个蜡烛的坐标
        left_list = [-1 for _ in range(len(s))]
        # 每一个下标左边第一个蜡烛的坐标
        right_list = [0 for _ in range(len(s))]
        r = -1  # 最左边为-1表示不存在
        for k, v in enumerate(s):
            if v == "*":
                prefix_sum += 1
            else:
                prefix_sum_dict[k] = prefix_sum
                r = k
            right_list[k] = r
        l = len(s)  # 最右边为len(s)表示不存在
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "|":
                l = i
            left_list[i] = l
        ans = []
        for left, right in queries:
            l_target = left_list[left]
            r_target = right_list[right]
            if l_target < r_target:
                ans.append(prefix_sum_dict[r_target] - prefix_sum_dict[l_target])
            else:
                ans.append(0)
        return ans
