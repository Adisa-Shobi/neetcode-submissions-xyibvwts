class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        allVisited = set()
        visited = set()
        children = [[] for i in range(n)]

        for a, b in edges:
            children[a].append(b)
            children[b].append(a)
        
        def dfs(curr, parent):
            if curr in allVisited:
                return False
            if curr in visited:
                return True
            
            visited.add(curr)
            for edg in children[curr]:
                if edg == parent:
                    continue
                if not dfs(edg, curr):
                    return False
            return True
        res = 0
        for i in range(n):
            visited = set()
            if dfs(i, -1):
                res += 1
            allVisited.update(visited)
        return res 