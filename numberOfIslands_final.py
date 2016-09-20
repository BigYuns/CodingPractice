"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) ==0: 
            return 0 

        checker = [[0 for c in range(len(grid[0]))] for r in range(len(grid))]
        counter = 1
        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                counter = self.dfs(r,c,grid,checker,counter)
        return counter-1
                
    def dfs(self,row,col,matrix,checker,counter): 
        if (matrix[row][col]== "1") and (not checker[row][col]): 
            checker[row][col] = counter
            if (col+1) < len(matrix[0]) and (matrix[row][col+1] == "1"):
                self.dfs(row, col+1, matrix,checker, counter)
            if (col-1) >= 0 and (matrix[row][col-1] == "1"): 
                self.dfs(row, col-1, matrix,checker,counter)
            if (row+1) < len(matrix) and (matrix[row+1][col] == "1"):
                self.dfs(row+1,col, matrix,checker, counter)
            if (row-1) >= 0 and (matrix[row-1][col] == "1"):
                self.dfs(row-1,col, matrix,checker,counter)
            counter = counter + 1 
        return counter 

"""
Comment: try with the untion find graph traversal method 
It will save the space complexity 
"""
