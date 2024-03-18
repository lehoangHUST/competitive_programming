class Solution:
    def addDigits(self, num: int) -> int:
        # Check num smaller than 10
        if num < 10:
            return num

        sum = 0
        while num >= 10:
            while num != 0:
                sum += num % 10
                num = num // 10
            
            num = sum
            sum = 0
        return num