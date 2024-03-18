class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Case 1: Iteration from 1 to k
        # for i in range(k):
        #     target = nums[-1]
        #     nums[1:] = nums[:-1]
        #     nums[0] = target

        # Case 2: Use divide
        n = len(nums)
        if k % n != 0:
            rotate = n - k % n
            target = nums[rotate:]
            nums[rotate:] = nums[0:rotate]
            nums[0:rotate] = target