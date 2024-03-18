import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        list_single_number = []
        for key, value in c.items():
            if value == 1:
                list_single_number.append(key)
        return list_single_number