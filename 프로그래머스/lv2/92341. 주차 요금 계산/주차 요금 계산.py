
import math

from datetime import datetime
from collections import defaultdict


def solution(fees, records):
    parking_time = _get_parking_time(records)
    
    parking_cost = defaultdict(float)   
    for car, time in parking_time.items():
        if time <= fees[0]:
            parking_cost[car] += fees[1]
            
        else:
            time -= fees[0]
            parking_cost[car] += fees[1] + math.ceil(time / fees[2]) * fees[3]
    
    parking_cost = sorted(parking_cost.items(), key=lambda x: x[0], reverse=False)
    
    return [cost for car, cost in parking_cost]


def _get_parking_time(records):
    parking = dict()
    parking_time = defaultdict(float)
        
    for record in records:
        time, car, status = record.split(" ")
        if car not in parking.keys():
            parking[car] = time
            continue
        
        minutes = _get_minutes(parking[car], time)
        parking_time[car] += minutes

        del parking[car]            
        
    for car, time in parking.items():
        minutes = _get_minutes(time, "23:59")
        
        parking_time[car] += minutes

    return parking_time


def _get_minutes(start_time, end_time):
    start_hour, start_minutes = start_time.split(":")
    end_hour, end_minutes = end_time.split(":")
    
    start_datetime = datetime(2023, 8, 21, int(start_hour), int(start_minutes), 0)
    end_datetime = datetime(2023, 8, 21, int(end_hour), int(end_minutes), 0)    
    
    elapsed = int((end_datetime - start_datetime).total_seconds() // 60)
    
    return elapsed
