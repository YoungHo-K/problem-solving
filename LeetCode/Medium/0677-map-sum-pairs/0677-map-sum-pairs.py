class MapSum:

    def __init__(self):
        self.map_dict = {}

    def insert(self, key: str, val: int) -> None:
        map_dict = self.map_dict
        
        for letter in key:
            if letter not in map_dict:
                map_dict[letter] = {}
            
            map_dict = map_dict[letter]
        
        map_dict["value"] = val
        
    def sum(self, prefix: str) -> int:
        map_dict = self.map_dict
        
        for letter in prefix:
            if letter not in map_dict:
                return 0
            
            map_dict = map_dict[letter]

        answer = 0
        stack = [(key, map_dict) for key in map_dict]
        while stack:
            key, tmp_map = stack.pop()
            if key == "value":
                answer += tmp_map[key]
                continue
                
            for next_key in tmp_map[key]:
                stack.append((next_key, tmp_map[key]))
                
        return answer                
            
        
            
            
            
            
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)