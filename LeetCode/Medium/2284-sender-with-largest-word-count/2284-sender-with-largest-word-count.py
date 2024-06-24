from collections import defaultdict


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_to_num_words = defaultdict(int)
        
        for sender, message in zip(senders, messages):
            sender_to_num_words[sender] += len(message.split(" "))

        max_num = 0
        answer = None
        for key, value in sender_to_num_words.items():
            if max_num < value:
                answer = key
                max_num = value
                
            elif max_num == value:
                if answer < key:
                    answer = key
            
        return answer        
        