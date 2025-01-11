class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        # Iterate till there is no carry 
        while (b & mask) != 0:
            
            # carry contains common set bits of a and b, left shifted by 1
            carry = (a & b) << 1

            # Update a with (a + b without carry)
            a = a ^ b
        
            # Update b with carry
            b = carry 
        
        return a & mask if b > 0 else a