# 가격이 떨어지지 않은 기간
def solution(prices):
    answer = []

    for i in range(len(prices)):
        p = prices[i]
        t = 0 # 가격이 떨어지지 않은 기간
        
        for j in range(i+1, len(prices)):
            t += 1
            if prices[j] < p: # 가격이 떨어지지 않을 때까지 시간+
                break
                
        answer.append(t)
        
    return answer