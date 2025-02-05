class Solution:
    def firstUniqChar(self, s: str) -> int:
        CountChar = {}
        for idx, char in enumerate(s):
            if char not in CountChar:
                CountChar[char] = []
            CountChar[char].append(idx)
        for char, list_idx_char in CountChar.items():
            if len(list_idx_char) == 1:
                return list_idx_char[-1]
        return -1