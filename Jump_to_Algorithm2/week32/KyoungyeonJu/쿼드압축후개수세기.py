def solution(arr):
    # 1. 확인 과정 len(arr) -> /2 -> 1
    # 2. 전체 같은 수인지 확인, 같다면
    # 3. 아니면, 4개 영역 나누기 0,0 0+l,0 0,0+l 0+l,0+l
    # 4. 2번에서부터 반복

    answer = []

    def check(r, c, l):
        if l == 1:
            answer.append(arr[r][c])
            return

        first = arr[r][c]  # 해당 영역의 가장 첫 번째 원소
        for i in range(r, r + l):
            for j in range(c, c + l):
                if first != arr[i][j]:
                    ll = l // 2
                    check(r, c, ll)  # 왼위
                    check(r, c + ll, ll)  # 오위
                    check(r + ll, c, ll)  # 왼아래
                    check(r + ll, c + ll, ll)  # 오아래
                    return

        answer.append(first)
        return

    check(0, 0, len(arr))

    return [answer.count(0), answer.count(1)]