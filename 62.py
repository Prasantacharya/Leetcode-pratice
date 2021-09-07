class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dpTable = [0]*n # rows are if you decide to go left
        for i in range(n):
            dpTable[i] = [0] * m # cols if you decide to go down
        
        for i in range(n):
            dpTable[i][0] = 1
        for i in range(m):
            dpTable[0][i] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dpTable[i][j] = dpTable[i - 1][j] + dpTable[i][j - 1]
        
        return dpTable[n - 1][m - 1]
