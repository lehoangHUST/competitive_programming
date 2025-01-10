class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        min_matrix = 0
        for row in range(rows):
            for col in range(cols):
                min_matrix += grid[row][col]
                if row == 0 and col != 0:
                    grid[row][col] += grid[row][col - 1]
                if col == 0 and row != 0:
                    grid[row][col] += grid[row - 1][col]
        # calculate sum
        for row in range(1, rows):
            for col in range(1, cols):
                min_matrix = min(grid[row - 1][col] + grid[row][col], grid[row][col - 1] + grid[row][col]) 
                grid[row][col] = min_matrix
        return min_matrix