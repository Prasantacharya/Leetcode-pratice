class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        def spread(grid, startI, startJ):
            if startI < 0 or startI >= len(grid) or startJ < 0 or startJ >= len(grid[0]) or (startI, startJ) in visited:
                return
            
            if grid[startI][startJ] == "1":
                visited.add((startI, startJ))
                spread(grid, startI + 1, startJ)
                spread(grid, startI - 1, startJ)
                spread(grid, startI, startJ + 1)
                spread(grid, startI, startJ - 1)
            
            return 
        
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    counter += 1
                    spread(grid, i, j)
        return counter
