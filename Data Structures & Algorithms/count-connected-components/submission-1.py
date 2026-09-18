class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        seen = set()

        def dfs(node):
            seen.add(node)
            for nei in adj_list[node]:
                if nei not in seen:
                    dfs(nei)

        comp = 0

        for i in range(n):
            if i not in seen:
                dfs(i)
                comp += 1
        
        return comp