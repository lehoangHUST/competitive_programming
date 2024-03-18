class Solution:
    def isHappy(self, n: int) -> bool:

        sum = -1
        list_sum = []
        while sum != 1:
            sum = 0
            while n != 0:
                sum += (n % 10) ** 2
                n = n // 10
            
            if sum in list_sum:
                return False
            else:
                list_sum.append(sum)
                n = sum
            print(n)
        return True