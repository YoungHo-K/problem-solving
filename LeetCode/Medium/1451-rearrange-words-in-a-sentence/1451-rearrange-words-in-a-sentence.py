

class Solution:
    def arrangeWords(self, text: str) -> str:
        lengths = []
        for index, word in enumerate(text.split(" ")):
            lengths.append((len(word), index, word.lower()))
            
        lengths.sort(key=lambda x: (x[0], x[1]))            
        
        answer = []
        for index in range(0, len(lengths)):
            word = lengths[index][2]
            if index == 0:
                word = word[0].upper() + word[1:]           
            
            answer.append(word)

        return " ".join(answer)
