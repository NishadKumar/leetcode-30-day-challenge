# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        row = len(matrix)
        column = len(matrix[0])
        
        result = [[0 for i in range(column + 1)] for i in range(row + 1)]
        height = 0
        
        for i in range(1, row + 1):
            for j in range(1, column + 1):
                if matrix[i-1][j-1] == '1':
                    result[i][j] = 1 + min(result[i-1][j], result[i][j-1], result[i-1][j-1])
                    height = max(height, result[i][j])
        
        return height ** 2