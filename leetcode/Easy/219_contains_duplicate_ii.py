class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Add dict
        dict_idx_nums = {}
        for index, num in enumerate(nums):
            if num not in dict_idx_nums.keys():
                dict_idx_nums[num] = [index]
            else:
                dict_idx_nums[num].append(index)
        
        print(dict_idx_nums)
        # 
        for key, value in dict_idx_nums.items():
            for i in range(0, len(value) - 1):
                for j in range(i + 1, len(value)):
                    if abs(value[i] - value[j]) <= k:
                        return True
        
        return False