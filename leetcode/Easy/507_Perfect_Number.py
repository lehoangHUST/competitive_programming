class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = self.getListDivisor(num)
        return sum(divisors) - num == num
    
    def getListDivisor(self, num):
        divisors = []
        i = 1
        while i * i <= num:
            if num % i == 0:
                j = num // i
                divisors.append(i)
                if j  != i:
                    divisors.append(j)
            i += 1
        return divisors