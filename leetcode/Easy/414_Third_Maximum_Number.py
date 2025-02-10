from math import inf
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_value = second_max_value = third_max_value = -inf
        for num in nums:
            if num in [max_value, second_max_value, third_max_value]:
                continue
            if num > max_value:
                third_max_value, second_max_value, max_value = second_max_value, max_value, num
            elif num > second_max_value:
                third_max_value, second_max_value = second_max_value, num
            elif num > third_max_value:
                third_max_value = num
        return third_max_value if third_max_value != -inf else max_value