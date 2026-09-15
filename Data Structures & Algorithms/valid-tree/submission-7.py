from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        q = deque([0])
        seen = {0}

        while q:
            node = q.popleft()
            for nei in adj_list[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)

        return len(seen) == n