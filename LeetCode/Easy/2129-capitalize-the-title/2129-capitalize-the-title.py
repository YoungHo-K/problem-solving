class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(" ")
        
        answer = []
        for word in title:
            word = word.lower()
            if len(word) > 2:
                word = word.capitalize()
            
            answer.append(word)
            
        return " ".join(answer)