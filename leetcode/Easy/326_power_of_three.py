import math

# Use logarit base 3

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Not value to 3^x = negative n
        if n <= 0:
            return False

        x = round(math.log(n, 3))
        if 3 ** x == n:
            return True
        else:
            return False
