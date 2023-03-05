import sys

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        lm = len(grid)
        ln = len(grid[0])

        tp = [[-1 for i in range(ln)] for j in range(lm)]
        tp[lm-1][ln-1] = grid[lm-1][ln-1]
        return self.minPath(0,0,lm,ln,grid,tp)

    def minPath(self,ri,rj,lm,ln,grid,tp):
        if ri >= lm or rj >= ln:
            return sys.maxsize
        
        if tp[ri][rj] != -1:
            return tp[ri][rj]
        
        tp[ri][rj] = grid[ri][rj] + min(self.minPath(ri+1,rj,lm,ln,grid,tp),self.minPath(ri,rj+1,lm,ln,grid,tp))

        return tp[ri][rj]