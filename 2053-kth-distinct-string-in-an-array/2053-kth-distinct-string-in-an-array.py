from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)

        answer = ""
        for value in arr:
            if counter[value] == 1:
                k -= 1
            
            if k == 0:
                answer = value
                break
                
        return answer
