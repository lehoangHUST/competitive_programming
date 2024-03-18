import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        exp = int(math.log2(n))
        if 2 ** exp == n:
            return True
        else:
            return False