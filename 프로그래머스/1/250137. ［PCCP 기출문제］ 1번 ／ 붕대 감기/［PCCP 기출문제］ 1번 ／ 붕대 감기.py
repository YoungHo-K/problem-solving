def solution(bandage, health, attacks):
    previous_attack_time = 0
    current_health = health
    for now_time, damage in attacks:
        duration = (now_time - previous_attack_time - 1)
        heal = duration * bandage[1] + (duration // bandage[0]) * bandage[2]        

        current_health = min(health, current_health + heal)
        
        current_health -= damage
        if current_health <= 0:
            current_health = -1
            break
        
        previous_attack_time = now_time
    
    return current_health