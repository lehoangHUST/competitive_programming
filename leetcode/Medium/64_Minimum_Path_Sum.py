class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Khởi tạo hàng đầu tiên và cột đầu tiên
        for row in range(1, rows):
            grid[row][0] += grid[row - 1][0]  # Tính tổng dọc cột đầu tiên
        for col in range(1, cols):
            grid[0][col] += grid[0][col - 1]  # Tính tổng ngang hàng đầu tiên
        
        # Tính toán các giá trị tối thiểu cho phần còn lại của ma trận
        for row in range(1, rows):
            for col in range(1, cols):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        
        return grid[-1][-1]