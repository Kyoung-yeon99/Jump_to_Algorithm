def solution(cards):  # 상자
    # 숫자 카드의 번호에 해당 하는 상자 인덱스
    idx = 0
    # 상자그룹들의 상자 개수
    box_sizes = []

    # 열어야 하는 상자가 이미 열려있을때까지 반복: 이미 열려있음을 표현해야 함(방문 체크)
    opened = [False] * len(cards)

    def find_box_size(idx):
        size = 0  # 초기화
        # 임의의 상자를 하나 선택 -> 선택 상자의 숫자 카드 확인
        while not opened[idx]:
            opened[idx] = True  # 상자를 엶
            idx = cards[idx] - 1  # 카드 번호에 해당하는 상자 인덱스로 이동(-1)
            size += 1  # 해당 상자그룹의 상자 개수 증가
        return size

    # 모든 상자 검사하면서 카드 찾음
    for i in range(len(cards)):
        if not opened[i]:  # 상자를 열지 않았다면
            box_sizes.append(find_box_size(i))

    # 그룹 크기가 2 이상이어야 계산가능
    if len(box_sizes) < 2:
        return 0
    # 최대 점수 뽑기
    box_sizes.sort(reverse=True)
    return box_sizes[0] * box_sizes[1]
