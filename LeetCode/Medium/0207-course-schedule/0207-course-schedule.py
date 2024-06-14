from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prep_course = defaultdict(list)
        for a, b in prerequisites:
            prep_course[a].append(b)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            if len(prep_course) == 0:
                return True
            
            visited.add(course)
            for first in prep_course[course]:
                if not dfs(first):
                    return False
                
            visited.remove(course)
            
            prep_course[course] = []            
            return True
        
        for course in range(0, numCourses):
            if not dfs(course):
                return False
            
        return True
