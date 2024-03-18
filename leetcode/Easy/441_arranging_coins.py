class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n == 1:
            return 1

        i = 0
        sum = 0
        while sum < n:
            sum += i
            i += 1
        
        if sum == n:
            return i - 1
        else:
            return i - 2