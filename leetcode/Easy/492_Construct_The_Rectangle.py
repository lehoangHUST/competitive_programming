class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        diff = area
        L, W = 0, 0
        i = 1
        while i * i <= area:
            if area % i == 0:
                j = area // i
                if diff > abs(j - i):
                    if j >= i:
                        L = j
                        W = i
                    else:
                        L = i
                        W = j
            i += 1
        return [L, W]