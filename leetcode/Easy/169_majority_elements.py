"""
    Solution
        + Step 1: Use library Counter to count element in list 
        + Step 2: Get max value of key in nums
"""
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        c_keys, c_values = list(c.keys()), list(c.values())
        results = c_keys[c_values.index(max(c_values))]
        return results