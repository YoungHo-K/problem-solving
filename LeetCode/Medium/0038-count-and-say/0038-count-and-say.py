
from collections import OrderedDict


class Solution:
    def countAndSay(self, n: int) -> str:
        string = "1"
        iteration = 1        
        while iteration < n:
            new_string = ""
            ch = string[0]
            count = 1
            for index in range(1, len(string)):
                if ch == string[index]:
                    count += 1
                
                else:
                    new_string += f"{count}{ch}"
                    ch = string[index]
                    count = 1
                    
            new_string += f"{count}{ch}"
            string = new_string            
            iteration += 1
            
        return string
                    