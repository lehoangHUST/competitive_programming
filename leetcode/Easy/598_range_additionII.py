class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        if len(ops) == 0: # check condition len(ops) == 0
            return m * n
        
        min_row, min_col = ops[0]
        for op in ops[1:]:
            row, col = op
            if row < min_row:
                min_row = row
            if col < min_col:
                min_col = col
        return min_row * min_col