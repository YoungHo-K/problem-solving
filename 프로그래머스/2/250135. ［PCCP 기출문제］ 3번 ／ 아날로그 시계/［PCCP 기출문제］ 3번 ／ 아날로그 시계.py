
def get_alert_count(hour, minute, second):
    count = (hour * 60 + minute) * 2 - hour
    
    second_angle = ((360 / 60) * second) % 360
    minute_angle = ((360 / 60) * minute + (360 / (60 * 60)) * second) % 360
    hour_angle = ((360 / 12) * hour + (360 / (12 * 60)) * minute + (360 / (12 * 60 * 60)) * second) % 360
    
    if second_angle >= minute_angle:
        count += 1
    
    if second_angle >= hour_angle:
        count += 1
    
    if hour >= 12:  
        count -= 2
                
    return count


def solution(h1, m1, s1, h2, m2, s2):
    answer = get_alert_count(h2, m2, s2) - get_alert_count(h1, m1, s1)
    
    if (h1 in [0, 12]) and (m1 == 0) and (s1 == 0):
        answer += 1
    
    return answer
    
            
        

#     if h1 in [0, 12] and m1 == 0 and s1 == 0:
#         ret += 1

#     return ret