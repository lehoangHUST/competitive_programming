class Solution:
    def longestConsecutive(self, nums) -> int:
        
        if len(nums) == 0:
            return 0
        
        set_nums = set(nums)
        longest = 0 
        
        for x in set_nums:
            if x - 1 not in set_nums:
                y = x + 1
                while y in set_nums:
                    y += 1
                longest = max(longest, y - x)
        return longest
