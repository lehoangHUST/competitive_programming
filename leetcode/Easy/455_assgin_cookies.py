class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # Bánh đủ lớn cho trẻ em này
                count += 1
                i += 1  # Xét đứa trẻ tiếp theo
            j += 1  # Luôn chuyển đến bánh tiếp theo

        return count