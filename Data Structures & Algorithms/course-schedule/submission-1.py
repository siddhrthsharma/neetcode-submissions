class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}

        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])

        seen = set()

        def dfs(crs):
            if crs in seen:
                return False

            if adj_list[crs] == []:
                return True
            
            seen.add(crs)

            for nei in adj_list[crs]:
                if not dfs(nei): return False
            
            seen.remove(crs)
            adj_list[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True