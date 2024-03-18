import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Count appear number in nums
        count = collections.Counter(nums)
        
        for num, appear in count.items():
            if appear == 1:
                return num