# from collections import deque

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:

#         q      = deque()
#         visits = set()
#         time   = 0

#         rows, cols = len(grid), len(grid[0])

#         # find all the initial ro-- fr--. ) O(m*n) time & space
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == 2:
#                     q.append((i,j))
#                     visits.add((i,j))
        
#         # finding the min time to ro-- the fr-- O(m*n) time and space
#         while q:
#             for i in range(len(q)):
#                 r, c = q.pop()
#                 neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
#                 for dr, dc in neighbors:
#                     r_curr = r+dr 
#                     c_curr = c+dc
#                     if min(r_curr,c_curr)<0 or r_curr==rows or c_curr==cols or grid[r_curr][c_curr]==0 or (r_curr,c_curr) in visits:
#                         continue
#                     q.append((r_curr, c_curr))
#                     visits.add((r_curr, c_curr))
#             # if len(q)>0:
#             time+=1
        
#         # checking if any fre-- fr-- left O(m*n)
#         c=0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]==1:
#                     c+=1
#                     if (i,j) not in visits:
#                         return -1
#         if c==0:
#             time=0
#         if c==1 and time!=0:
#             time=1
#         return time

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q      = deque()
        visits = set()
        time   = 0

        rows, cols = len(grid), len(grid[0])

        # find all the initial ro-- fr--. ) O(m*n) time & space
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visits.add((i,j))

        # finding the min time to ro-- the fr-- O(m*n) time and space
        while q:
            for i in range(len(q)):
                # r, c = q.pop()
                r, c = q.popleft()  # CHANGED: oldest first (a queue); pop() took the newest and mixed minutes
                neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in neighbors:
                    r_curr = r+dr
                    c_curr = c+dc
                    if min(r_curr,c_curr)<0 or r_curr==rows or c_curr==cols or grid[r_curr][c_curr]==0 or (r_curr,c_curr) in visits:
                        continue
                    q.append((r_curr, c_curr))
                    visits.add((r_curr, c_curr))
            if len(q)>0:  # CHANGED: your line, uncommented: a minute counts only if this pass rotted a fruit
                time+=1   # CHANGED: indented

        # checking if any fre-- fr-- left O(m*n)
        # c=0  # REMOVED, with every c line below: the two changes cover these cases
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    # c+=1
                    if (i,j) not in visits:
                        return -1
        # if c==0:
        #     time=0
        # if c==1 and time!=0:
        #     time=1
        return time

        




        


        