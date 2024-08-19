# https://school.programmers.co.kr/learn/courses/30/lessons/131130

# 1번 상자 그룹에 속한 상자의 수와 2번 상자 그룹에 속한 상자의 수를 곱한 값의 최댓값
def solution(cards):
    answer = 0
    N = len(cards)
    
    def open_box(cur_idx, opened):
        group = []
        while True:
            opened[cur_idx] = True
            group.append(cards[cur_idx])
            cur_idx = cards[cur_idx] - 1 # 다음으로 열 상자 번호
            if opened[cur_idx]: # 이미 연 상자라면 종료
                break
        
        return group, opened
    
    for i in range(N): # i: 처음 열 상자
        group1, opened = open_box(i, [False for _ in range(N)])        
        for j in range(N):
            if cards[j] not in group1: # j: 두 번째 그룹에서 처음 열 상자
                group2, opened = open_box(j, opened)
                answer = max(answer, len(group1) * len(group2))
        
    return answer