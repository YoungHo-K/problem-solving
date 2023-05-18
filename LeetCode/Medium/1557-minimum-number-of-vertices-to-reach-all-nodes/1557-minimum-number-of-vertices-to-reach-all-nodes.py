class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        answer = {key: 0 for key in range(0, n)}
        
        for from_node, to_node in edges:
            if to_node in answer.keys():
                del answer[to_node]
                
        return answer
        
        