import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False

        x = round(math.log(n, 4))
        if 4 ** x == n:
            return True
        else:
            return False