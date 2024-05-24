
class TopScore:
    def __init__(self, length):
        self.length = length
        self.scores = []        
        
    def add(self, value):
        self.scores.append(value)
        self.scores.sort()
            
        if self.length <= len(self.scores):
            self.scores = self.scores[-self.length:]
            
    def present(self):
        return self.scores[0]

    
def solution(k, score):
    top_score = TopScore(length=k)
    
    answer = []    
    for value in score:
        top_score.add(value)
        
        answer.append(top_score.present())
    
    return answer