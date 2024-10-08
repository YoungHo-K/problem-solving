from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_info = defaultdict(list)
        for a, b in prerequisites:
            course_info[a].append(b)
        
        finished = [0] * numCourses
        answer = []
        def dfs(course):
            if finished[course] == 1:
                return True
            
            if finished[course] == -1:
                return False
            
            finished[course] = -1
            
            is_cycle = False
            for pre in course_info[course]:
                if not dfs(pre):
                    is_cycle = True
                    break
            
            if is_cycle:
                return False
                
            finished[course] = 1
            answer.append(course)
            
            return True
        
        is_cycle = False
        for course in range(0, numCourses):
            if not dfs(course):
                is_cycle = True
                break
        
        return answer if not is_cycle else []
    