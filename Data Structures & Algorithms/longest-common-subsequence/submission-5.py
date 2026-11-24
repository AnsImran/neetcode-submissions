# This one is without memoization. I worked it out myself and for the memoization we had to ask an AI to add memoization to it. 

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         t1       = text1
#         t2       = text2
#         i,j      = 0,0
#         seq      = []
#         seq_lens = []
#         cache    = {}

#         def dfs(i, j, t1, t2, seq, seq_lens, cache):
#             if i>=len(t1) or j>=len(t2):
#                 return
#             if (i,j) in cache:
#                 return cache[(i,j)]
#             if t1[i]==t2[j]:
#                 seq.append(t1[i])
#                 seq_lens.append(len(seq))
#                 # cache[(i,j)] = seq_lens[-1]
#                 dfs(i+1, j+1, t1, t2, seq, seq_lens, cache)
#                 seq.pop()
#             else:
#                 dfs(i+1, j,   t1, t2, seq, seq_lens, cache)
#                 # if len(seq_lens)>0:
#                 #     cache[(i+1,j)] = seq_lens[-1]

#                 dfs(i,   j+1, t1, t2, seq, seq_lens, cache)

#                 # if len(seq_lens)>0:
#                 #     cache[(i,j+1)] = seq_lens[-1]            
        
#         dfs(i, j, t1, t2, seq, seq_lens, cache)
#         if len(seq_lens)>0:
#             return max(seq_lens)
#         else:
#             return 0


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1       = text1
        t2       = text2
        i,j      = 0,0
        # seq      = []
        # seq_lens = []
        cache    = {}

        def dfs(i, j, t1, t2, cache):
            if i>=len(t1) or j>=len(t2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if t1[i]==t2[j]:
                cache[(i,j)] = 1 + dfs(i+1, j+1, t1, t2,  cache)
            else:
                cache[(i,j)] = max(dfs(i+1, j,   t1, t2,  cache),
                                   dfs(i,   j+1, t1, t2,  cache))
            return cache[(i,j)]

        return dfs(i, j, t1, t2,  cache)






        