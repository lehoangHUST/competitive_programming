class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
            Trailing 0s in n! = Count of 5s in prime factors of n!
                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
        """
        if n == 0:
            return 0

        count_zero = 0
        i = 1
        while (n // 5 ** i) != 0:
            count_zero += n // 5 ** i
            i += 1
        return count_zero