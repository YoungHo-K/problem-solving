class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def _backtracking(string, left_cnt, right_cnt, result):
            if left_cnt > 0:
                _backtracking(string + "(", left_cnt - 1, right_cnt, result)
            
            if left_cnt < right_cnt:
                _backtracking(string + ")", left_cnt, right_cnt - 1, result)
             
            if right_cnt == 0:
                result.append(string)
                
            return result
        
        return _backtracking("", n, n, [])