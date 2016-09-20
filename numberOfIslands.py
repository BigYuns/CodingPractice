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
        #if self.isBaseCase(row,col,matrix,checker,counter): 
            #return counter
        
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
        
    #def isBaseCase(self,r,c,grid,checker,counter): 
        """
        This function checks whether a specific cell is a base case.
        If the cell is a base case, return true.
        If not, return false 
        """
        #return (grid[r][c] == 0 or self.isOutOfRange(r,c,grid) or checker[r][c]==1) 
    
    #def isOutOfRange(self,r,c,grid): 
        """
        This function checks whether the given indices, each of which represents row and col respectively, are out of range. 
        if it is out of range, return true
        if not return false 
        """
        #return (r<0 or c<0 or r>=(len(grid)) or c>=(len(grid[0]))) 


"""
Using Map 
"""

def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))