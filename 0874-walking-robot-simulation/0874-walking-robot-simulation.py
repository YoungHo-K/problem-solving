class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        
        answer = 0
        dx, dy = 0, 1        
        pos_x, pos_y = 0, 0
        for cmd in commands:
            if cmd < 0:
                dx, dy = (-dy, dx) if cmd == -2 else (dy, -dx)
                continue
            
            for _ in range(0, cmd):
                next_x = pos_x + dx
                next_y = pos_y + dy                
                if (next_x, next_y) in obstacles:
                    break
                
                pos_x, pos_y = next_x, next_y
                
            answer = max(answer, pos_x ** 2 + pos_y ** 2)
                
        return answer
