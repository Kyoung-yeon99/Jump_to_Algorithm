from math import ceil

def fee_cal(time, fees):
    # 기본 시간 이하인 경우 기본 요금 반환
    if time <= fees[0]:
       return fees[1]
    else:
        # 초과 시간 계산
        ex_time = time - fees[0]
        # 초과 시간을 단위 시간으로 나누어 올림 계산
        unit_time = ceil(ex_time / fees[2])
        #print("단위 시간:", unit_time)
        # 최종 요금 반환
        return fees[1] + fees[3] * unit_time

    
    print(time)
def time_diff(in_t, out_t):
    #분으로 변환 후 빼기
    in_h, in_m = map(int, in_t.split(':'))
    out_h, out_m = map(int, out_t.split(':'))
    
    in_minutes = in_h*60 + in_m
    out_minutes = out_h*60 + out_m
    
    #print(out_minutes - in_minutes)
    return out_minutes - in_minutes

def solution(fees, records):
    #차량번호 별로 누적 주차 시간 구해서 요금 계산
    car_io = {} #입/출차 상태
    parking_time = {} #누적 주차시간
    #처음에 차량번호로 주차 상태, 주차시간 초기화
    for record  in records:
        t, car_num, io = record.split()
        car_io[car_num] = "F"
        parking_time[car_num]=0
        
    for record  in records:
        t, car_num, io = record.split()
        
        if car_io[car_num]=="F" or io=="IN": #차 넣으면
            car_io[car_num]=(t, io) #"입차 시간","IN" 업데이트
        elif io == "OUT": #출차 시 누적 주차시간 계산
            i_t, _ = car_io[car_num] #입차 시간 가져오기
            parking_time[car_num]+=time_diff(i_t,t) #누적 시간 업데이트
            car_io[car_num]=(t, io) #"출차 시간", "OUT" 업데이트
    
    #출차 내역 확인
    for car_num in car_io:
        if car_io[car_num][1] == "IN": #안나간 차 있으면 누적 시간 업데이트
            i_t, _ = car_io[car_num]
            parking_time[car_num]+=time_diff(i_t,'23:59')
    
    #주차 요금 계산
    answer = []
    
    #차량 번호가 작은 자동차부터
    car_num_keys = car_io.keys()
    car_num_keys = sorted(list(car_num_keys))
    
    for car_num in car_num_keys:
        answer.append(fee_cal(parking_time[car_num],fees))
    

    return answer
