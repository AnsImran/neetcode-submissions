class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        r     = 0
        c     = 0
        cache = {}
        grid  = obstacleGrid

        def tpdp(r, c, rows, cols, grid, cache):
            if r==rows or c==cols:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            if grid[r][c]==1:
                return 0
            if r==rows-1 and c==cols-1:
                return 1
            
            paths = tpdp(r+1, c, rows, cols, grid, cache) + tpdp(r, c+1, rows, cols, grid, cache)
            cache[(r,c)] = paths
            return paths

        ans = tpdp(r, c, rows, cols, grid, cache)
        return ans













        