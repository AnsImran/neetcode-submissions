class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def create_adj_list(prerequisites):
            adj_list = {}
            for src, dst in prerequisites:
                if src in adj_list:
                    adj_list[src].append(dst)
                else:
                    adj_list[src] = [dst]
            return adj_list
        
        def graph_dfs(node, visits, adj_list, visits_main, ans_main):
            if node in visits:
                return 1
            if node in visits_main:      # NEW: already proven safe, skip
                return

            visits.add(node)
                                         # REMOVED: visits_main.add(node) from here
            for neighbor in adj_list.get(node, []):
                ans = graph_dfs(neighbor, visits, adj_list, visits_main, ans_main)
                if ans:
                    ans_main.add(ans)
            visits.remove(node)
            visits_main.add(node)        # MOVED: mark finished only after exploring
            return

        adj_list = create_adj_list(prerequisites)

        visits_main = set()
        visits      = set()
        ans_main    = set()

        for node in adj_list.keys():
            if node in visits_main:
                continue
            else:
                graph_dfs(node, visits, adj_list, visits_main, ans_main)
                if 1 in ans_main:
                    return False

        
        return True

            