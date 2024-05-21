
class Date:
    def __init__(self, date_str: str):
        date_str = date_str.split(".")
        
        self.year = int(date_str[0])
        self.month = int(date_str[1])
        self.day = int(date_str[2])

    def add(self, month: int):
        if month > 12:
            self.month += month % 12
            self.year += month // 12
        else:
            self.month += month
                        
        if self.month > 12:
            self.month -= 12
            self.year += 1

    
def solution(today, terms, privacies):
    term_to_duration = {}
    for term in terms:
        term, duration = term.split(" ")
        term_to_duration[term] = int(duration)
        
    answer = []
    today = Date(today)
    for index, privacy in enumerate(privacies):
        date_str, term = privacy.split(" ")             
        due_date = Date(date_str)
        due_date.add(term_to_duration[term])
        
        if due_date.year < today.year:
            answer.append(index + 1)
            
        elif (due_date.year == today.year) and (due_date.month < today.month):
            answer.append(index + 1)
            
        elif (due_date.year == today.year) and (due_date.month == today.month) and (due_date.day <= today.day):
            answer.append(index + 1)

    return answer