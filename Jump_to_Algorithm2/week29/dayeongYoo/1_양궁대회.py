def solution(n, info):  # n: 라이언이 쏠 수 있는 화살 개수, info: 어피치 과녁 점수
    answer = []  # 라이언이 최적의 화살 분배를 했을 때 결과 저장 리스트
    ryan = [0] * 11  # 라이언이 각 과녁에 몇 발의 화살을 맞췄는지 저장하는 리스트
    diff = 0  # 현재까지 라이언과 어피치의 점수 최대차

    # m: 라이언이 쏜 화살 수, idx: 현재 탐색하는 과녁 번호
    def dfs(m, idx):
        nonlocal answer, diff, ryan  # 함수 내부에서 수정가능하게끔

        # 백트래킹 기저 조건: 화살을 모두 쏜 경우
        if m == n:
            # 점수 계산
            r, a = 0, 0

            # 각 점수 영역(10점~0점)에서 라이언과 어피치 점수 비교
            for j in range(11):
                if ryan[j] > info[j]:  # 라이언이 더 많은 화살 쏜 경우
                    r += 10 - j  # 해당 점수는 라이언이 획득
                elif info[j] > 0:  # 라이언이 하나도 화살 못 쐈을때, 어피치가 해당 과녁에 쏜 경우
                    a += 10 - j  # 해당 점수는 어피치가 획득
            # 라이언의 점수가 더 높은 경우
            if r > a:
                # 현재 최대 점수차보다 더 큰 경우에만 업데이트
                if diff < r - a:
                    diff = r - a
                    answer = ryan[:]  # 깊은 복사: ryan의 요소가 변동되어도 answer는 변하지 x
                # 점수 차이가 같은 경우, 더 낮은 점수에 화살을 많이 쏜 경우를 선택
                elif diff == r - a:
                    for i in range(10, -1, -1):  # 루프가 역순으로 실행: 0~10점까지 검토
                        if ryan[i] < answer[i]:  # answer보다 적은 화살 쐈다면 종료
                            break
                        elif ryan[i] > answer[i]:  # answer보다 많은 화살 쐈다면
                            answer = ryan[:]  # 정답 갱신
                            break
            return  # 모든 화살을 다 쏘고 결과 계산이 끝나면, 탐색 종료

        # 각 과녁 점수를 하나씩 탐색
        for i in range(idx, 11):
            ryan[i] += 1  # 현재 과녁 점수에 화살 하나 추가
            dfs(m + 1, i)  # 다음 화살 쏘기 위한 재귀 호출
            ryan[i] -= 1  # 현재 과녁 점수 초기화(최적해를 찾기 위해)

    dfs(0, 0)
    return answer if answer else [-1]
