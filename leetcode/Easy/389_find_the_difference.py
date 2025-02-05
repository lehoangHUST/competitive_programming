from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if s == "":
            return t
        
        DictChar_s = dict(Counter(s))
        DictChar_t = dict(Counter(t))
        for char, num_char in DictChar_t.items():
            if char not in DictChar_s:
                return char
            else:
                if DictChar_s[char] != DictChar_t[char]:
                    return char