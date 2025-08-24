class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # store dict freq
        freq_count = {}
        for num in nums:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1
        
        # sum unique
        ans = 0
        for num in freq_count:
            if freq_count[num] != 1:
                continue
            ans += num
        return ans