class TreeNode:
    def __init__(self, val):
        self.val = val
        self.edges = []

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {}
        for i in range(n):
            nodes[i] = TreeNode(i)
        
        for a, b in edges:
            nodes[a].edges.append(nodes[b])
            nodes[b].edges.append(nodes[a])
        
        visited = set()
        def dfs(node, parent):
            if node.val in visited:
                return False
            visited.add(node.val)
            for edg in node.edges:
                if edg.val == parent:
                    continue
                if not dfs(edg, node.val):
                    return False
            
            return True
        if not dfs(nodes[0], -1):
            return False
        return len(visited) == n
                                                                     