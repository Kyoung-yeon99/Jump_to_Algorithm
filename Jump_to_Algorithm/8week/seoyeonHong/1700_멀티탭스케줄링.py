# 플러그를 빼는 횟수 최소화
n, k = map(int, input().split()) # 멀티탭 구멍의 개수, 전기 용품의 총 사용횟수
order = list(map(int, input().split())) # 전기용품 사용 순서
using = [] # 멀티탭에 꽂은 전기용품 목록
change_num = 0

for i in range(k):
    num = order[i] # 사용할 전기용품 번호
    if num not in using:
        if len(using) == n: # 교체해야 할 경우
            # 가장 나중에 사용하게 될 전자용품 교체
            max_idx = 0
            change = 0
            for u in using:
                if u not in order[i:]: # 앞으로 사용되지 않을 경우 교체
                    change = u
                    break
                else: # 앞으로 사용되는 경우 가장 나중에 다시 사용될 전기용품 교체
                    idx = order[i:].index(u)  
                    if idx > max_idx:
                        max_idx = idx
                        change = u
            using.remove(change)
            using.append(num)
            change_num += 1
        else: # 콘센트 자리가 남은 경우 교체 없이 꽂기
            using.append(num)

print(change_num)