class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def matrix_dfs(grid, r, c, visits, counts):
            rows, cols, = len(grid),len(grid[0])
            if (r,c) in visits or min(r,c)<0  or r==rows or c==cols or grid[r][c]==0:
                return

            if grid[r][c] == 1:
                counts.append(1)

            visits.add((r,c))
            # or comment out the above line, and put `grid[r][c] = 0` in place of `visits.remove((r,c))`. 

            matrix_dfs(grid, r+1, c,   visits, counts)
            matrix_dfs(grid, r-1, c,   visits, counts)
            matrix_dfs(grid, r,   c+1, visits, counts)
            matrix_dfs(grid, r,   c-1, visits, counts)

            # visits.remove((r,c))
            # or grid[r][c] = 0
            return

        visits = set()
        area   = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                counts = []
                if grid[r][c]==0 or (r,c) in visits:
                    continue
                else:
                    matrix_dfs(grid, r, c, visits, counts)
                    current_area = len(counts)
                    if current_area > area:
                        area = current_area
        return area
            



        