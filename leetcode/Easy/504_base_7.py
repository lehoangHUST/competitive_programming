class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return "0"

        # Check sign negative or positive
        sign = False
        if num < 0:
            num = -num
            sign = True

        string_base7 = ""
        while num > 0:
            string_base7 += str(num % 7)
            num = num // 7
        
        if sign:
            return '-' + string_base7[::-1]
        else:
            return string_base7[::-1]