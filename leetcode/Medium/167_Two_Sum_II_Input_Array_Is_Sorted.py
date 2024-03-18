class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(numbers):
            if (target - num) in numbers[i + 1:]:
                return [i + 1, numbers[i + 1:].index(target - num) + i + 1 + 1]