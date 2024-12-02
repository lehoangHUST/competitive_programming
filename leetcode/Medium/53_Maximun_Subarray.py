class Solution:
    def maxSubArray(self, nums) -> int:
        
        res = nums[0]
        maxEnding = nums[0]
        
        for num in nums[1:]:
            
            maxEnding = max(maxEnding + num, num)
            res = max(res, maxEnding)
        return res