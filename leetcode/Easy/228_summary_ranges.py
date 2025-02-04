class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                ranges.append(f"{start}" if start == nums[i - 1] else f"{start}->{nums[i - 1]}")
                start = nums[i]
        
        ranges.append(f"{start}" if start == nums[-1] else f"{start}->{nums[-1]}")
        return ranges