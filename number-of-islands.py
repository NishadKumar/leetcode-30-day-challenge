# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        islands = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += self.check_island(i, j, grid)
        
        return islands
    
    def check_island(self, i, j, grid):
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == '0':
            return 0
        
        grid[i][j] = '0'
        
        self.check_island(i + 1, j, grid)
        self.check_island(i - 1, j, grid)
        self.check_island(i, j + 1, grid)
        self.check_island(i, j - 1, grid)
        
        return 1