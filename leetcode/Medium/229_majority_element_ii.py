import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        
        c = collections.Counter(nums)
        c = { key: value for key, value in c.items() if value > threshold }
        return list(c.keys())