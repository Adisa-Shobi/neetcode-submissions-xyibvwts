class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for c, p in prerequisites:
            pre[c].append(p)
        
        output = []
        path, visit = set(), set()
        def dfs(c):
            if c in path:
                return False
            if c in visit:
                return True
            
            path.add(c)
            for course in pre[c]:
                if dfs(course) == False:
                    return False
            path.remove(c)

            visit.add(c)
            output.append(c)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output
            

