import math
def solution(fees, records):
    ans = []
    basic_time, basic_fee, per_min, plus_fee = fees 
    
    car = {}
    for idx in records:
        idx = idx.split()
        car[idx[1]] = 0
        
    dic = {}
    for idx in records:
        idx = idx.split()
        temp = idx[0].split(':')
        in_time = int(temp[0]) * 60 + int(temp[1])
        
        if idx[2] == 'IN':
            dic[idx[1]] = in_time
        
        elif idx[2] == 'OUT':
            if idx[1] in dic.keys():
                car[idx[1]] += in_time - dic[idx[1]]
                dic[idx[1]] = -1
    
    for key, value in dic.items():
        if value != -1:
            car[key] = car[key] + (1439 - dic[key])
            
        
    for key,value in car.items():
        if value <= basic_time: 
            ans.append((int(key),basic_fee)) 

        elif value > basic_time:
            tot_fee = basic_fee + math.ceil((value - basic_time)/per_min) * plus_fee
            ans.append((int(key),tot_fee))
    
    ans.sort(key = lambda x: x[0])
    real_ans = []
    for key, money in ans:
        real_ans.append(money)
    
    return real_ans
    
