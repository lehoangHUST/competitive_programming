class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # Tính tổng ban đầu của F(0) và tổng tất cả các phần tử trong nums
        total = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        
        maxValue = F
        
        # Dùng công thức để tính F(k) từ F(k-1)
        for idx in range(1, n):
            F += total - n * nums[-idx]
            maxValue = max(maxValue, F)
        
        return maxValue