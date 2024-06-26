class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        answer = 0
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        n, m = len(version1), len(version2)
        
        if n < m:
            version1 += ["0"] * (m - n)
                    
        if m < n:
            version2 += ["0"] * (n - m)
        
        for index in range(0, max(n, m)):
            value_1 = int(version1[index])
            value_2 = int(version2[index])

            if value_1 < value_2:
                answer = -1
                break
            
            if value_1 > value_2:
                answer = 1
                break
                        
        return answer
