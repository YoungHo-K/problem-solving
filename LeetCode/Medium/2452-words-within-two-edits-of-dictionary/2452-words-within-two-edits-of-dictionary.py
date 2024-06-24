

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answer = []
        
        for query in queries:            
            for target in dictionary:
                diff = 0
                for index in range(0, len(query)):
                    if query[index] != target[index]:
                        diff += 1
                        continue
                        
                if diff <= 2:
                    answer.append(query)
                    break
        
        return answer
