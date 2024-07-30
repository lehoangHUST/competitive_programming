import numpy as np

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = np.array(matrix)
        spiral = []
        
        while matrix.size != 0:
            spiral += list(matrix[0, :])
            matrix = np.delete(matrix, 0, 0)
            matrix = np.rot90(matrix)
            
        return spiral