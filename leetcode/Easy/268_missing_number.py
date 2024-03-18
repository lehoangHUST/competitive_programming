class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        """
        Case 1: Not use math

        for i in range(n + 1):
            if i not in nums:
                return i
        """

        # Case 2: Use math for find missing Number
        sum_nums = sum(nums) 
        sum_n = ((n + 1) * (n + 0)) // 2
        return sum_n - sum_nums