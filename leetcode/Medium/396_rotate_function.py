class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        maxValue = 0
        for idx, num in enumerate(nums):
            maxValue += idx * num
        
        n = len(nums)
        total = sum(nums)
        F = maxValue
        # consider value
        for idx in range(1, n):
            F += total - n * nums[n - idx]
            maxValue = max(maxValue, F)
        
        return maxValue