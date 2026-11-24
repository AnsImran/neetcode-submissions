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

# Hey I solved this with the top-bottom technique of 2D dynamic programming in the NEET code lessons but I think it's pretty straightforward to do it via bottom-up dynamic programming as well (which a lot of people think is the true dynamic problem). Kindly create that solution as well for me and all the visualizations for that as well so that I can go through them later as well. Right now for the previous problem I did it with the bottom-up approach. For this one I am doing it with top-bottom so that, given the limited time that I have, I get some practice on both. 













        