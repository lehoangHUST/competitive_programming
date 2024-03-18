import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        
        for key, value in c.items():
            if value == 1:
                return key