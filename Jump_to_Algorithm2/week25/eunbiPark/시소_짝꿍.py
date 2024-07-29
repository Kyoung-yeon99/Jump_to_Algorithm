from collections import defaultdict
def solution(weights):
    # 몸무게, 시소거리의 비율을 곱한 값 등록 
    # 같은 (몸무게 * 비율) 탐색 
    ans = 0
    dic = {}
    ratio = [1/1, 1/2, 2/1, 2/3, 3/2, 3/4, 4/3] # 모든 비율
    
    dic = defaultdict(float)
    
    # 몸무게와 시소 거리의 모든 경우의 수
    for w in weights:
        for r in ratio:
            ans += dic[r * w]
        dic[w] += 1

    return int(ans)
