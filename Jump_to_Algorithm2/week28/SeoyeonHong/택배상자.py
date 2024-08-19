# https://school.programmers.co.kr/learn/courses/30/lessons/131704

# 두 개의 컨테이너 벨트를 사용하여 실을 수 있는 상자의 개수
def solution(order):
    cnt = 0
    original = [i for i in range(len(order), 0, -1)] # 기존 컨테이너
    stored = [] # 보조 컨테이너
    
    for o in order:
        moved = False # 트럭으로 상자를 실었는지
        if original and original[-1] == o: # 기존 컨테이너 -> 트럭
            original.pop()
            moved = True
        elif stored and stored[-1] == o: # 보조 컨테이너 -> 트럭
            stored.pop()
            moved = True
        elif original: # 기존 컨테이너에서 원하는 상자가 나올 때까지 꺼내기
            while original:
                b = original.pop()
                if b == o: # 기존 컨테이너 -> 트럭
                    moved = True
                    break
                else: # 기존 컨테이너 -> 보조 컨테이너
                    stored.append(b)
        if not moved: # 원하는 상자를 실지 못했을 경우 종료
            break
        cnt += 1
    
    return cnt