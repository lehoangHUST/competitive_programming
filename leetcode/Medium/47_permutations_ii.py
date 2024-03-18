"""
    Combine with idea in problem 46 => Use condition check list in permutations
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

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
            for p in self.permuteUnique(remList):
                
                # Maybe use type set in pythons
                
                l = [m] + p
                if l not in permutions: 
                    permutions.append([m] + p)
        
        return permutions