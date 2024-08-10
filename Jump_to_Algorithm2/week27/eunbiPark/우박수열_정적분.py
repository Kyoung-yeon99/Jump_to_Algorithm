def solution(k, ranges):
    # 사다리꼴 넓이, 구간합
    area = []
    while k > 1:
        prev_k = k
        if k % 2 == 0:
            k /= 2
        else:
            k = k*3 + 1
        area.append((prev_k + k) / 2)
        
    total = len(area)
    ans = []
    for a, b in ranges:
        b = total + b
        snum = sum(area[a:b]) if a <= b else -1
        ans.append(snum)
    
    return ans 
    
