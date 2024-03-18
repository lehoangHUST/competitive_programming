class Solution:

    def NewtonMethod(self, num):
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num


    def BitwiseTrick(self, num):
        root = 0
        bit = 1 << 15
        
        while bit > 0 :
            root |= bit
            if root > num // root:    
                root ^= bit                
            bit >>= 1        
        return root * root == num


    def Math(self, num):
            i = 1
            while (num>0):
                num -= i
                i += 2       
            return num == 0

    def BinarySearch(self, num):
            left = 0
            right = num
            
            while left <= right:
                mid = left + (right-left)//2
                if  mid ** 2 == num:
                    return True
                elif mid ** 2 > num:
                    right = mid -1
                else:
                    left = mid +1
            return False



    def Linear(self, num):
            i = 1
            while i ** 2 <= num:
                if i ** 2 == num:
                    return True
                else:
                    i += 1
            return False


    def isPerfectSquare(self, num: int) -> bool:
        isPerfect = self.NewtonMethod(num)
        return isPerfect        return False