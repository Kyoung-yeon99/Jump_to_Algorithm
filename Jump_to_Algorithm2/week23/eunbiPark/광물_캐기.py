def solution(picks, minerals):
    total = sum(picks) * 5 # 캘 수 있는 광물의 수 
    # 캘 수 있는 만큼만 광물 자르기
    minerals = minerals[:min(len(minerals), total)]
    
    # 조사 
    cnt = [[0, 0, 0] for _ in range(10)] # 다이아, 철, 돌 하나의 곡괭이로 캘 수 있는 돌의 유형을 조사, minerals의 최대 길이 <= 50 이기에 5개씩 10그룹 -> range(50)
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cnt[i//5][0] += 1 
        elif minerals[i] == 'iron':
            cnt[i//5][1] += 1
        else:
            cnt[i//5][2] += 1
   
    # 피로도가 높은 순서대로 정렬
    cnt.sort(key = lambda x: (-x[0], -x[1], -x[2]))
    # cnt.sort(key = lambda x: (x[2], x[1], x[0])) # 이건 안된다
    
    # 피로도 계산
    ans = 0
    for m in cnt:
        d, i, s = m
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0: # 다이아를 쓸 수 있을 때 
                picks[p] -= 1
                ans += (d + i + s)
                break
            elif p == 1 and picks[p] > 0:
                picks[p] -= 1
                ans += (5 * d + i + s)
                break
            elif p == 2 and picks[p] > 0:
                picks[p] -= 1
                ans += (25 * d + 5 * i + s)
                break
                
    return ans
                    
                
    