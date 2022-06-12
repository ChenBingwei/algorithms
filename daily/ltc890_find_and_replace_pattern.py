from typing import List


class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_list = self.format_pattern(pattern)
        ans = []
        for word in words:
            if self.format_pattern(word) == pattern_list:
                ans.append(word)
        return ans

    def format_pattern(self, word):
        tmp_dict = {}
        start = 0
        result = []
        for w in word:
            if w not in tmp_dict:
                tmp_dict[w] = start
                start += 1
            result.append(tmp_dict[w])
        return result
