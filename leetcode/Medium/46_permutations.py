"""
    A -> B -> C
      -> C -> B
    B -> A -> C
      -> C -> A
    C -> B -> A
      -> A -> B
    => 6 examples
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Check empty list nums
        if len(nums) == 0:
            return []
        
        # Check list nums is only element
        if len(nums) == 1:
            return [nums]

        permutions = []

        # Iterate the input(lst) and calculate the permutation
        for i in range(len(nums)):
            m = nums[i]

            remList = nums[:i] + nums[i + 1:]
            
            # Generate permutions
            for p in self.permute(remList):
                permutions.append([m] + p)
        
        return permutions